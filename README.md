## API для учета личных доходов и расходов

### Основные технологии
Python 3.10     
FastAPI 0.86.0   
Pydantic 1.10.2   
SQLAlchemy 1.4.43  
Uvicorn 0.19.0

### Запуск проекта в dev-режиме
- Склонируйте репозиторий:  
``` git clone <название репозитория> ```    
- Установите и активируйте виртуальное окружение:  
``` python -m venv venv ```  
``` source venv/Scripts/activate ``` 
- Установите зависимости из файла requirements.txt:   
``` pip install -r requirements.txt ```
- Создайте в папке FastAPI_budget файл .env и пропишите в нем:   
JWT_SECRET=<ваш_набор_символов>   
пример: JWT_SECRET=^JSDH7kjsd*kasldl
- Для запуска сервера выполните команду:   
``` python -m budget ``` 

##### После запуска сервера будет доступна документация к API по адресам:
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
