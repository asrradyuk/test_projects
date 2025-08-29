# FastAPI Learning Project

Проект для изучения FastAPI с современной архитектурой.

## Архитектура
- **Repository Pattern** - разделение логики доступа к данным
- **Модульные роутеры** - организация эндпоинтов по модулям
- **Pydantic схемы** - валидация входящих/исходящих данных
- **Async SQLAlchemy** - асинхронная работа с базой данных

## Структура проекта
project/
├── models/         # ORM модели
├── repositories/   # Доступ к данным
├── schemas/        # Pydantic схемы
├── routers/        # HTTP контроллеры
├── database.py     # Настройка БД
└── main.py         # Точка входа

## Установка и запуск
```bash
pip install fastapi uvicorn sqlalchemy aiosqlite
uvicorn main:app --reload