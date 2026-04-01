# UniMarket 🛒

Платформа для покупки и продажи товаров между студентами университета.

## Технологии

- **Backend**: FastAPI 0.104+
- **Database**: PostgreSQL + SQLAlchemy
- **Python**: 3.10+

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/YOUR_USERNAME/UniMarket.git
cd UniMarket
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл `.env` (скопируйте из `.env.example`):
```bash
cp .env.example .env
```

5. Запустите сервер:
```bash
python src/main.py
```

6. Откройте документацию:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Структура проекта

```
UniMarket/
├── src/                  # Исходный код
│   ├── main.py           # Точка входа
│   ├── config.py         # Конфигурация
│   ├── models/           # SQLAlchemy модели
│   ├── schemas/          # Pydantic схемы
│   ├── routers/          # API endpoints
│   └── utils/            # Вспомогательные функции
├── tests/                # Тесты
├── alembic/              # Миграции БД
├── .env.example          # Пример переменных окружения
└── requirements.txt      # Зависимости
```

## Разработка

Установите pre-commit hooks:
```bash
pre-commit install
```

## API Endpoints

| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/` | Главная страница |
| GET | `/health` | Проверка работоспособности |
| GET | `/about` | Информация о проекте |
| GET | `/docs` | Swagger UI документация |
