from database.models import User, Couple, Wish
from database.db import session

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from exceptions import *

async def get_all_users_from_db():
    async with session() as sess:
        query = select(User)
        result = await sess.execute(query)
        return result.scalars().all()

async def get_user_from_db(user_id: int) -> User | None:
    async with session() as sess:
        query = select(User).filter_by(id=user_id)
        result = await sess.execute(query)
        res: User | None = result.scalar_one_or_none()
        if res:
            return res
        raise NoUserFoundError()
    
async def add_user_to_db(user_id: int, username: str, couple_id: int = None):
    async with session() as sess:
        try:
            await get_user_from_db(user_id)
            raise UserAlreadyExistsError()
        except NoUserFoundError:
        
            new_user = User(id=user_id, username=username, couple_id=couple_id)
            sess.add(new_user)

            try:
                await sess.commit()
                return new_user
            except:
                await sess.rollback()
        
async def update_user_in_db(user_id: int, username: str, couple_id: int):
    try:
        user = await get_user_from_db(user_id)
    except NoUserFoundError:
        raise NoUserFoundError()
    else:
        if user:
            async with session() as sess:
                user.username = username
                user.couple_id = couple_id
                try:
                    await sess.commit()
                except:
                    await sess.rollback()


async def delete_user_from_db(user_id: int):
    pass

async def get_all_couples_from_db():
    async with session() as sess:
        query = select(Couple).options(selectinload(Couple.users))
        result = await sess.execute(query)
        return result.scalars().all()


async def create_couple(user1_id: int, user2_id: int) -> Couple:
    async with session() as sess:
        user1 = await get_user_from_db(user1_id)
        user2 = await get_user_from_db(user2_id)
        couple = Couple(users=[user1, user2])
        sess.add(couple)
        try:
            await sess.commit()
        except:
            await sess.rollback()

async def get_couple_from_db(couple_id: int) -> Couple | None:
    async with session() as sess:
        query = select(Couple).filter_by(id=couple_id)
        result = await sess.execute(query)
        res: Couple | None = result.scalar_one_or_none()
        return res if res else None
    