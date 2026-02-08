from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship, DeclarativeBase
from typing import Optional

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    couple_id: Mapped[Optional[int]] = mapped_column(ForeignKey("couples.id"))
    couple: Mapped[Optional["Couple"]] = relationship(back_populates="users")

class Couple(Base):
    __tablename__ = "couples"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    users: Mapped[list["User"]] = relationship(back_populates="couple", cascade="all")
    wishes: Mapped[list["Wish"]] = relationship(cascade="all, delete-orphan")

class Wish(Base):
    __tablename__ = "wishes"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str]
    price: Mapped[float]
    article: Mapped[int]
    url: Mapped[str]
    couple_id: Mapped[int] = mapped_column(ForeignKey("couples.id"))
    user_added_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    