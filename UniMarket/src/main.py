# src/main.py
"""
Главный файл приложения UniMarket
"""
from fastapi import FastAPI
from config import settings


# Создаем приложение FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Платформа для покупки и продажи товаров между студентами",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",  # ReDoc документация
)


@app.get("/")
async def root():
    """
    Корневой endpoint - приветствие
    """
    return {
        "message": "Добро пожаловать в UniMarket!",
        "version": settings.VERSION,
        "docs": "/docs",
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint - проверка работоспособности
    """
    return {"status": "healthy", "project": settings.PROJECT_NAME}


@app.get("/about")
async def about():
    """
    About endpoint - информация о проекте
    """
    return {
        "project": "UniMarket",
        "description": "Студенческий маркетплейс",
        "author": "Ваше имя",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Автоперезагрузка при изменении кода
    )
