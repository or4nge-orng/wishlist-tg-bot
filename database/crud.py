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
            if not couple_id:
                # Явно загружаем пару и её пользователей
                stmt = select(Couple).where(Couple.id == user.couple_id).with_for_update()
                result = await sess.scalars(stmt)
                couple = result.one_or_none()
                print(couple.id)
                if couple:
                    # Подсчитываем, сколько пользователей в паре (до удаления)
                    user_count = await sess.scalar(
                        select(func.count()).select_from(User).where(User.couple_id == couple.id)
                    )
                    if user_count <= 1:
                        await sess.delete(couple)
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
        query = select(Couple)\
            .options(selectinload(Couple.users), selectinload(Couple.wishes))\
            .filter_by(id=couple_id)
        result = await sess.execute(query)
        res: Couple | None = result.scalar_one_or_none()
        if res:
            return res
        raise NoCoupleFoundError()

async def create_couple(user1_id: int, user2_id: int | None = None) -> Couple:
    async with session() as sess:
        # Загружаем пользователей
        user1 = await sess.get(User, user1_id)
        if not user1:
            raise NoUserFoundError(user1_id)

        user2 = None
        if not user2_id:
            user2 = await sess.get(User, user2_id)
            if not user2:
                raise NoUserFoundError(user2_id)

        # Формируем список без None
        users = [user1]
        if user2:
            users.append(user2)

        # Создаём пару
        couple = Couple(users=users)
        sess.add(couple)

        try:
            await sess.commit()
            await sess.refresh(couple)  # чтобы подгрузить id и связи
            return couple
        except Exception as e:
            await sess.rollback()
            print(f"Error in create_couple: {e}")  # ← для отладки
            raise CoupleCreationError() from e

        
async def update_couple_in_db(couple_id: int, user1_id: int, user2_id: int):
    async with session() as sess:
        # Загружаем всё в одной сессии
        couple = await sess.get(Couple, couple_id, options=[selectinload(Couple.users)])
        if not couple:
            raise NoCoupleFoundError()

        user1 = await sess.get(User, user1_id)
        if not user1:
            raise NoUserFoundError(user1_id)

        user2 = await sess.get(User, user2_id) if user2_id else None
        if user2_id and not user2:
            raise NoUserFoundError(user2_id)

        # Отвязываем пользователей от старых пар (если нужно — SQLAlchemy сделает сам, но проверим)
        # Просто присваиваем новых пользователей — relationship позаботится об обновлении couple_id
        couple.users = [user1, user2] if user2 else [user1]

        try:
            await sess.commit()
            await sess.refresh(couple)  # Обновляем объект после коммита
        except Exception as e:
            await sess.rollback()
            print(f"DB Error in update_couple_in_db: {e}")  # ← Для отладки
            raise CoupleUpdateError() from e

async def delete_couple_from_db(couple_id: int):
    async with session() as sess:
        couple = await sess.get(Couple, couple_id)
        if not couple:
            raise NoCoupleFoundError(couple_id)
        await sess.delete(couple)
        try:
            await sess.commit()
        except:
            await sess.rollback()
            raise CoupleDeleteError()



async def get_all_wishes_from_db():
    async with session() as sess:
        query = select(Wish)
        result = await sess.execute(query)
        return result.scalars().all()
    
async def get_wish_from_db(wish_id: int) -> Wish:
    async with session() as sess:
        query = select(Wish).filter_by(id=wish_id)
        result = await sess.execute(query)
        res: Wish | None = result.scalar_one_or_none()
        if res:
            return res
        raise NoWishFoundError()
    
async def add_wish_to_db(name: str, price: float, couple_id: int, user_added_id: int, article: int = 0, url: str = '') -> Wish:
    async with session() as sess:
        couple = await sess.get(Couple, couple_id)
        user_added = await sess.get(User, user_added_id)
        if not couple:
            raise NoCoupleFoundError(couple_id)
        
        if not user_added:
            raise NoUserFoundError(user_added_id)

        wish = Wish(name=name, price=price, article=article, user_added_id=user_added_id, url=url, couple_id=couple_id)
        sess.add(wish)
        try:
            await sess.commit()
            await sess.refresh(wish)
            return wish
        except Exception as e:
            await sess.rollback()
            print(f"Error in add_wish_to_db: {e}")  # ← для отладки
            raise WishCreationError()