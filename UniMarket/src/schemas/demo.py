from pydantic import BaseModel, Field, validator
from typing import Optional
from typing import List
class ItemCreate(BaseModel):
 """Схема для создания товара"""
 name: str = Field(..., min_length=3, max_length=100, description="Название товара")
 description: Optional[str] = Field(None, max_length=500, description="Описание товара")
 price: int = Field(..., gt=0, description="Цена в рублях (должна быть больше 0)")
 category: str = Field(..., description="Категория товара")
 @validator('price')
 def price_must_be_positive(cls, v):
    if v <= 0:
        raise ValueError('Цена должна быть больше нуля')
    return v
 @validator('name')
 def name_must_not_be_empty(cls, v):
    if not v.strip():
        raise ValueError('Название не может быть пустым')
    return v.strip()
 class Config:
    json_schema_extra = {
 "example": {
 "name": "Учебник по Python",
 "description": "Отличное состояние, год издания 2023",
 "price": 500,
 "category": "books" } }
class ItemResponse(BaseModel):
 """Схема ответа с информацией о товаре"""
 id: int
 name: str
 description: Optional[str]
 price: int
 category: str
 status: str = "active"
 class Config:
    json_schema_extra = {
 "example": {
 "id": 1,
 "name": "Учебник по Python",
 "description": "Отличное состояние",
 "price": 500,
 "category": "books",
 "status": "active" } }
class UserCreate(BaseModel):
 """Схема для регистрации пользователя"""
 username: str = Field(..., min_length=3, max_length=50)
 email: str = Field(..., description="Email адрес")
 password: str = Field(..., min_length=6, description="Пароль (минимум 6 символов)")
 @validator('email')
 def email_must_be_valid(cls, v):
    if '@' not in v:
        raise ValueError('Некорректный email адрес')
    return v.lower()
 class Config:
    json_schema_extra = {
 "example": {
 "username": "student123",
 "email": "student@university.edu",
 "password": "secure_password_123" } }
class UserResponse(BaseModel):
 """Схема ответа с информацией о пользователе"""
 id: int
 username: str
 email: str
 role: str = "student"
 class Config:
    json_schema_extra = {
 "example": {
 "id": 1,
 "username": "student123",
 "email": "student@university.edu",
 "role": "student" } }

class ItemListResponse(BaseModel):
    """Схема для списка товаров с метаданными"""
    total: int = Field(..., description="Общее количество товаров")
    items: List[ItemResponse] = Field(..., description="Список товаров")
    
    class Config:
        json_schema_extra = {
            "example": {
                "total": 2,
                "items": [
                    {
                        "id": 1,
                        "name": "Учебник Python",
                        "description": "Новый",
                        "price": 500,
                        "category": "books",
                        "status": "active"
                    }
                ]
            }
        }
class MessageResponse(BaseModel):
 """Стандартный ответ с сообщением"""
 message: str
 details: Optional[dict] = None