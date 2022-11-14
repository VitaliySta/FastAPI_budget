from fastapi import FastAPI

from .api import router


tags_metadata = [
    {
        'name': 'auth',
        'description': 'Регистрация и авторизация',
    },
    {
        'name': 'operations',
        'description': 'Работа с операциями',
    },
    {
        'name': 'reports',
        'description': 'Импорт/экспорт данных',
    },
]

app = FastAPI(
    title='Budget',
    description='Сервис учета личных доходов и расходов',
    version='1.0.0',
    openapi_tags=tags_metadata,
)
app.include_router(router)
