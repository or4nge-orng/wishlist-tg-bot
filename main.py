from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi import status

from database.db import engine
from database.models import Base

from database.crud import *
from database.dto import *

from exceptions import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#=========USERS=========#
@app.get("/users/", response_model=List[Users])
async def get_users():
    users = await get_all_users_from_db()
    return users

@app.get("/users/{user_id}/", response_model=User)
async def get_user_by_id(user_id: int):
    try:
        user = await get_user_from_db(user_id)
        return user
    except NoUserFoundError as e:
        return HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, content=str(e))

@app.post("/users/")
async def add_user(user: UserCreate):
    try:
        new_user = await add_user_to_db(user.id, user.username)
        return new_user
    except UserAlreadyExistsError as e:
        return HTMLResponse(status_code=status.HTTP_409_CONFLICT, content=str(e))
    except UserCreationError as e:
        return HTMLResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=str(e))
    
@app.put("/users/{user_id}")
async def update_user(user_id: int, user: UserUpdate):
    try:
        if user.username:
            await update_user_in_db(user_id, user.username, user.couple_id)
            return {"status": "success"}
        else:
            return {"status": "error", "message": "No username provided"}
    except NoUserFoundError as e:
        return HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, content=str(e))
    except UserUpdateError as e:
        return HTMLResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=str(e))
        
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    try:
        await delete_user_from_db(user_id)
        return {"status": "success"}
    except NoUserFoundError as e:
        return HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, content=str(e))
    except UserDeleteError as e:
        return HTMLResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=str(e))

@app.get("/couples/", response_model=List[CoupleWithUsers])
async def get_couples():
    couples = await get_all_couples_from_db()
    return couples
    
@app.get("/couples/{couple_id}", response_model=CoupleDetail)
async def get_couple_by_id(couple_id: int):
    try:
        couple = await get_couple_from_db(couple_id)
        return couple
    except NoCoupleFoundError as e:
        return HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, content=str(e))
        

@app.post("/couples/")
async def add_couple(new_couple: CoupleCreate):
    try:
        couple = await create_couple(new_couple.user1_id, new_couple.user2_id)
        return couple
    except NoUserFoundError as e:
        return HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, content=str(e))
    except CoupleCreationError as e:
        return HTMLResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=str(e))

@app.put("/couples/{couple_id}")
async def update_couple(couple_id: int, couple: CoupleUpdate):
    try:
        if couple.user1_id:
            await update_couple_in_db(couple_id, couple.user1_id, couple.user2_id)
            return {"status": "success"}
        else:
            return HTMLResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Не передано user1_id")
    except NoCoupleFoundError as e:
        return HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, content=str(e))
    except NoUserFoundError as e:
        return HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, content=str(e))
    except CoupleUpdateError as e:
        return HTMLResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=str(e))

@app.delete("/couples/{couple_id}")
async def delete_couple(couple_id: int):
    try:
        await delete_couple_from_db(couple_id)
        return {"status": "success"}
    except NoCoupleFoundError as e:
        return HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, content=str(e))

@app.get("/wishes/", response_model=List[Wish])
async def get_wishes():
    wishes = await get_all_wishes_from_db()
    if wishes:
        return wishes
    return HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, content="Желаний не найдено")

@app.get("/wishes/{wish_id}", response_model=Wish)
async def get_wish_by_id(wish_id: int):
    try:
        wish = await get_wish_from_db(wish_id)
        return wish
    except NoWishFoundError as e:
        return HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, content=str(e))

@app.post("/wishes/")
async def add_wish(wish: WishCreate):
    try:
        if wish.couple_id:
            new_wish = await add_wish_to_db(wish.name, wish.price, wish.couple_id, wish.user_added_id, wish.article, wish.url)
            return new_wish
        else:
            return HTMLResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Не передано couple_id")
    except NoCoupleFoundError as e:
        return HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, content=str(e))
    except NoUserFoundError as e:
        return HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, content=str(e))
    except WishCreationError as e:
        return HTMLResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=str(e))
    
@app.put("/wishes/{wish_id}")
async def update_wish(wish_id: int, wish: WishUpdate):
    if wish.name:
        try:
            await edit_wish_in_db(wish_id, wish.name, wish.price, wish.article, wish.url, wish.image)
            return {"status": "success"}
        except NoWishFoundError as e:
            return HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, content=str(e))
        except WishUpdateError as e:
            return HTMLResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=str(e))
        
@app.delete("/wishes/{wish_id}")
async def delete_wish(wish_id: int):
    try:
        await delete_wish_from_db(wish_id)
        return {"status": "success"}
    except NoWishFoundError as e:
        return HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, content=str(e))
    except WishDeleteError as e:
        return HTMLResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=str(e))
