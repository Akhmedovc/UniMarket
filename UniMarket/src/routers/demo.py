from fastapi import APIRouter, HTTPException
from typing import Optional # Добавляем импорт
from src.schemas.demo import (ItemCreate, ItemResponse, UserCreate, UserResponse) 
from src.schemas.demo import ItemListResponse, MessageResponse
router = APIRouter(
 prefix="/demo",
 tags=["Demo"])
@router.get("/users/{user_id}")
async def get_user(user_id: int):
 """
 Получить пользователя по ID
 Args:
 user_id: ID пользователя (целое число)
 Returns:
 dict: Информация о пользователе
 """
 # Имитация данных (позже будет из БД)
 fake_users = {
 1: {"id": 1, "name": "Алиса", "role": "student"},
 2: {"id": 2, "name": "Боб", "role": "student"},
 3: {"id": 3, "name": "Кэрол", "role": "admin"} }
 if user_id not in fake_users:
    raise HTTPException(
 status_code=404,
 detail=f"Пользователь с ID {user_id} не найден" )
 return fake_users[user_id]
@router.get("/items/{item_id}")
async def get_item(item_id: int):
 """
 Получить товар по ID
 Args:
 item_id: ID товара
 Returns:
 dict: Информация о товаре
 """
 # Имитация данных
 fake_items = {
 1: {"id": 1, "name": "Учебник по Python", "price": 500},
 2: {"id": 2, "name": "Ноутбук Dell", "price": 25000},
 3: {"id": 3, "name": "Настольная лампа", "price": 800} }

 if item_id not in fake_items:
    raise HTTPException(
 status_code=404,
 detail=f"Товар с ID {item_id} не найден" )
 return fake_items[item_id]
@router.get("/categories/{category_name}")
async def get_category(category_name: str):
 """
 Получить товары по категории
 Args:
 category_name: Название категории
 Returns:
 dict: Список товаров в категории
 """
 # Имитация данных по категориям
 categories = {
 "books": [
 {"id": 1, "name": "Python для начинающих"},
 {"id": 2, "name": "Алгоритмы и структуры данных"}
 ],
 "electronics": [
 {"id": 3, "name": "Ноутбук"},
 {"id": 4, "name": "Наушники"}
 ],
 "furniture": [
 {"id": 5, "name": "Стол"},
 {"id": 6, "name": "Стул"}
 ]
 }
 if category_name not in categories:
    raise HTTPException(
 status_code=404,
 detail=f"Категория '{category_name}' не найдена" )
 return {
 "category": category_name,
 "items": categories[category_name],
 "count": len(categories[category_name])
 }

@router.get("/search/items")
async def search_items(
 name: Optional[str] = None,
 price_min: Optional[int] = None,
 price_max: Optional[int] = None,
 category: Optional[str] = None
):
 """
 Поиск товаров с фильтрами
 Args:
 name: Поиск по названию (необязательно)
 price_min: Минимальная цена (необязательно)
 price_max: Максимальная цена (необязательно)
 category: Категория товара (необязательно)
 Returns:
 dict: Найденные товары и параметры поиска
 """
 # Все товары (имитация)
 all_items = [
 {"id": 1, "name": "Учебник Python", "price": 500, "category": "books"},
 {"id": 2, "name": "Ноутбук Dell", "price": 25000, "category": "electronics"},
 {"id": 3, "name": "Лампа настольная", "price": 800, "category": "furniture"},
 {"id": 4, "name": "Учебник Java", "price": 600, "category": "books"},
 {"id": 5, "name": "Мышка Logitech", "price": 1200, "category": "electronics"}
 ]
 # Фильтруем
 filtered_items = all_items.copy()
 if name:
   iltered_items = [
 item for item in filtered_items
 if name.lower() in item["name"].lower()
 ]
 if price_min is not None:
   filtered_items = [
 item for item in filtered_items
 if item["price"] >= price_min
 ]
 if price_max is not None:
   filtered_items = [
 item for item in filtered_items
 if item["price"] <= price_max
 ]
 if category:
   filtered_items = [
 item for item in filtered_items
 if item["category"] == category
 ]
 return {
 "filters": {
 "name": name,
 "price_min": price_min,
 "price_max": price_max,
 "category": category
 },
 "total_found": len(filtered_items),
 "items": filtered_items
 }
@router.get("/search/users")
async def search_users(
 role: Optional[str] = None,
 limit: int = 10,
 offset: int = 0
):
 """
 Поиск пользователей с пагинацией
 Args:
 role: Фильтр по роли (student/admin)
 limit: Количество результатов (по умолчанию 10)
 offset: Смещение для пагинации (по умолчанию 0)
 Returns:
 dict: Найденные пользователи
 """
 # Имитация базы пользователей
 all_users = [
 {"id": 1, "name": "Алиса", "role": "student"},
 {"id": 2, "name": "Боб", "role": "student"},
 {"id": 3, "name": "Кэрол", "role": "admin"},
 {"id": 4, "name": "Дэвид", "role": "student"},
 {"id": 5, "name": "Ева", "role": "admin"},
 {"id": 6, "name": "Фрэнк", "role": "student"},
 ]
 # Фильтр по роли
 filtered_users = all_users
 if role:
   filtered_users = [u for u in all_users if u["role"] == role]
 # Пагинация
 paginated_users = filtered_users[offset:offset + limit]
 return {
 "filters": {"role": role},
 "pagination": {
 "limit": limit,
 "offset": offset,
 "total": len(filtered_users)
 },
 "users": paginated_users }

fake_items_db = []
fake_users_db = []
next_item_id = 1
next_user_id = 1

@router.post("/items", response_model=ItemResponse, status_code=201)
async def create_item(item: ItemCreate):
 """
 Создать новый товар
 Args:
 item: Данные товара
 Returns:
 ItemResponse: Созданный товар с ID
 """
 global next_item_id
 new_item = {
 "id": next_item_id,
 "name": item.name,
 "description": item.description,
 "price": item.price,
 "category": item.category,
 "status": "active" }
 fake_items_db.append(new_item)
 next_item_id += 1
 return new_item
@router.post("/users", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate):
 """
 Зарегистрировать нового пользователя
 Args:
 user: Данные пользователя
 Returns:
 UserResponse: Созданный пользователь с ID
 """
 global next_user_id
 # Проверяем уникальность email
 if any(u["email"] == user.email for u in fake_users_db):
    raise HTTPException(
 status_code=400,
 detail="Пользователь с таким email уже существует" )
 new_user = {
 "id": next_user_id,
 "username": user.username,
 "email": user.email,
 "role": "student"
 }
 fake_users_db.append(new_user)
 next_user_id += 1
 return new_user
@router.get("/items/all", response_model=list[ItemResponse])
async def get_all_items():
 """
 Получить все созданные товары
 Returns:
 list: Список всех товаров
 """
 return fake_items_db
@router.get("/users/all", response_model=list[UserResponse])
async def get_all_users():
 """
 Получить всех зарегистрированных пользователей

 Returns:
 list: Список всех пользователей
 """
 return fake_users_db

@router.get("/items/list", response_model=ItemListResponse)
async def get_items_list():
 """
 Получить список товаров с метаданными
 Returns:
 ItemListResponse: Список товаров и общее количество
 """
 return {
 "total": len(fake_items_db),
 "items": fake_items_db }
@router.delete("/items/{item_id}", response_model=MessageResponse)
async def delete_item(item_id: int):
 """
 Удалить товар по ID
 Args:
 item_id: ID товара для удаления
 Returns:
 MessageResponse: Сообщение об успешном удалении
 """
 global fake_items_db
 # Ищем товар
 item_index = None
 for i, item in enumerate(fake_items_db):
    if item["id"] == item_id:
        item_index = i
        break
 if item_index is None:
    raise HTTPException(
 status_code=404,
 detail=f"Товар с ID {item_id} не найден" )
 deleted_item = fake_items_db.pop(item_index)
 return {
 "message": f"Товар '{deleted_item['name']}' успешно удален",
 "details": {"deleted_item_id": item_id} }