from database.models import User, Couple, Wish
from database.db import session

from sqlalchemy import func, select
from sqlalchemy.orm import selectinload

from exceptions import *

# ----- User Cruds -----

async def get_all_users_from_db():
    async with session() as sess:
        query = select(User)
        result = await sess.execute(query)
        return result.scalars().all()

async def get_user_from_db(user_id: int) -> User:
    async with session() as sess:
        query = select(User).filter_by(id=user_id)
        result = await sess.execute(query)
        res: User | None = result.scalar_one_or_none()
        if res:
            return res
        raise NoUserFoundError(user_id)
    
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
                raise UserCreationError()
        
async def update_user_in_db(user_id: int, username: str, couple_id: int):
    async with session() as sess:
        user = await sess.get(User, user_id)
        if user:
            user.username = username if username else user.username
            user.couple_id = couple_id if couple_id else None
            try:
                await sess.commit()
            except:
                await sess.rollback()
                raise UserUpdateError()
        else:
            raise NoUserFoundError()

async def delete_user_from_db(user_id: int):
    async with session() as sess:
        # Получаем пользователя
        user = await sess.get(User, user_id)
        if not user:
            raise NoUserFoundError(user_id)

        couple = None
        if user.couple_id:
            # Явно загружаем пару и её пользователей
            stmt = select(Couple).where(Couple.id == user.couple_id).with_for_update()
            result = await sess.scalars(stmt)
            couple = result.one_or_none()

            if couple:
                # Подсчитываем, сколько пользователей в паре (до удаления)
                user_count = await sess.scalar(
                    select(func.count()).select_from(User).where(User.couple_id == couple.id)
                )
                if user_count <= 1:
                    await sess.delete(couple)

        # Удаляем пользователя
        await sess.delete(user)
        try:
            await sess.commit()
        except:
            await sess.rollback()
            raise UserDeleteError()

# ----- Couple Cruds -----

async def get_all_couples_from_db():
    async with session() as sess:
        query = select(Couple).options(selectinload(Couple.users))
        result = await sess.execute(query)
        return result.scalars().all()

async def get_couple_from_db(couple_id: int) -> Couple:
    async with session() as sess:
        query = select(Couple).filter_by(id=couple_id)
        result = await sess.execute(query)
        res: Couple | None = result.scalar_one_or_none()
        if res:
            return res
        raise NoCoupleFoundError()

async def create_couple(user1_id: int, user2_id: int = None):
    async with session() as sess:
        user1 = await get_user_from_db(user1_id)
        user2 = await get_user_from_db(user2_id) if user2_id else None
        couple = Couple(users=[user1, user2])
        sess.add(couple)
        try:
            await sess.commit()
            return couple
        except:
            await sess.rollback()
            raise CoupleCreationError()
