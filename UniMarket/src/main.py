import sys
import os
from fastapi import FastAPI

# Настройка путей (оставляем как есть)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ПРЯМОЙ ИМПОРТ: так Python точно увидит переменную router внутри файлов
from src.routers.system import router as system_router
from src.routers.demo import router as demo_router
from src.config import settings

tags_metadata = [
    {
        "name": "System",
        "description": "Системные проверки статуса API и базы данных.",
    },
    {
        "name": "Demo",
        "description": "Демонстрационные эндпоинты для товаров и пользователей.",
    },
]

app = FastAPI(
 title=settings.PROJECT_NAME,
 version=settings.VERSION,
 description="""
 ## UniMarket API
 Платформа для покупки и продажи товаров между студентами университета.
 ### Возможности:
 * **Товары**: Создание, поиск, фильтрация товаров
 * **Пользователи**: Регистрация и управление профилями
 * **Категории**: Организация товаров по категориям
 * **Поиск**: Мощный поиск с фильтрами

 ### Технологии:
 * FastAPI
 * SQLAlchemy
 * PostgreSQL
 """,
 openapi_tags=tags_metadata,
 docs_url="/docs",
 redoc_url="/redoc",
    contact={
    "name": "UniMarket Team",
    "email": "support@unimarket.edu"
 },
 license_info={
    "name": "MIT" })
# Подключаем роутеры
app.include_router(system_router)
app.include_router(demo_router)
@app.get("/", tags=["Root"])
async def root():
 """
 Корневой endpoint - приветствие и навигация
 Returns:
 dict: Приветственное сообщение и ссылки на документацию
 """
 return {
 "message": "Добро пожаловать в UniMarket API!",
 "version": settings.VERSION,
 "documentation": {
 "swagger": "/docs",
 "redoc": "/redoc"
 },
 "endpoints": {
 "system": "/system/health",
 "demo": "/demo" } }
if __name__ == "__main__":
 import uvicorn
 uvicorn.run(
 "src.main:app",
 host="172.29.80.1",
 port=8080,
 reload=True )
