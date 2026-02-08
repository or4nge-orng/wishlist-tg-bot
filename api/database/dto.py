from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from datetime import datetime

# ----- Wish модели -----
class WishBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255, description="Название товара", example="Новый iPhone")
    price: float = Field(..., ge=0, description="Цена товара", example=999.99)

class WishCreate(WishBase):
    couple_id: int = Field(None, description="ID пары, для которой создается желание")
    article: int = Field(None, ge=0, description="Артикул товара")
    url: str = Field(None, min_length=0, description="Ссылка на товар")
    image: str = Field(None, min_length=0, description="Ссылка на изображение товара")
    user_added_id: int = Field(None, description="ID пользователя, добавившего желание")

class WishUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    price: Optional[float] = Field(None, ge=0)
    article: Optional[int] = Field(None, ge=0)
    url: Optional[str] = Field(None, min_length=0)
    image: Optional[str] = Field(None, min_length=0)
    
    @field_validator('price')
    def price_positive(cls, v):
        if v is not None and v < 0:
            raise ValueError('Цена должна быть больше 0')
        return v

class Wish(WishBase):
    id: int
    article: int
    url: str
    image: str
    couple_id: int
    user_added_id: int
    
    class Config:
        from_attributes = True

# ----- User модели -----
class UserBase(BaseModel):
    id: int = Field(..., example=1)

class UserCreate(UserBase):
    username: Optional[str] = Field(None, min_length=3, max_length=50, example="test")
    couple_id: Optional[int] = Field(None, description="ID пары, к которой присоединить пользователя")

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    couple_id: Optional[int] = Field(None, description="ID пары для присоединения, 0 для выхода из пары")

class UserInCouple(BaseModel):
    """Модель пользователя для отображения внутри пары"""
    id: int
    username: str
    
    class Config:
        from_attributes = True

class Users(UserBase):
    id: Optional[int] = None
    username: Optional[str] = None
    couple_id: Optional[int] = None

    class Config:
        from_attributes = True

class User(Users):
    
    message: Optional[str] = "success"
    status: Optional[bool] = True

    class Config:
        from_attributes = True

# ----- Couple модели -----
class CoupleBase(BaseModel):
    pass

class CoupleCreate(CoupleBase):
    user1_id: Optional[int] = Field(None, description="ID первого пользователя")
    user2_id: Optional[int] = Field(None, description="ID второго пользователя")

class Couple(CoupleBase):
    id: int
    
    class Config:
        from_attributes = True

class CoupleWithUsers(Couple):
    users: List[UserInCouple] = []

class CoupleWithWishes(Couple):
    wishes: List[Wish] = []

class CoupleDetail(Couple):
    """Полная информация о паре"""
    users: List[UserInCouple] = []
    wishes: List[Wish] = []

class CoupleUpdate(BaseModel):
    user1_id: Optional[int] = Field(None, description="ID первого пользователя")
    user2_id: Optional[int] = Field(None, description="ID второго пользователя")

# ----- Response модели -----
class MessageResponse(BaseModel):
    message: str

class UserWithCouple(User):
    couple: Optional[Couple] = None