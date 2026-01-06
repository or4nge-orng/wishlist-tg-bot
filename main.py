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
    except NoUserFoundError:
        raise HTMLResponse(status_code=status.HTTP_404_NOT_FOUND, )

@app.post("/users/")
async def add_user(user: UserCreate):
    try:
        new_user = await add_user_to_db(user.id, user.username)
        return new_user
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@app.put("/users/{user_id}")
async def update_user(user_id: int, user: UserUpdate):
    pass
    

@app.post("/add_couple/{user1_id}/{user2_id}")
async def add_couple(user1_id: int, user2_id: int):
    try:
        await create_couple(user1_id, user2_id)
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/get_couples", response_model=list[CoupleWithUsers])
async def get_couples():
    try:
        couples = await get_all_couples_from_db()
        return couples
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    try:
        await delete_user_from_db(user_id)
        return {"status": "success"}
    except NoUserFoundError:
        return {"status": "error", "message": "No user in database"}
