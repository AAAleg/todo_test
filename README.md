# TODO

#### Установка неоходимых библиотек:
```bash
pip install -r requirements.txt
```

#### Запуск проекта:
```bash
./manage.py migrate
./manage.py runserver
```

# Интерактивная документация API (Swagger)
http://localhost:8000/api/docs

# Документация API

## Регистрация
**POST /api/sign_up/**
```
{
  "email": "test@test.ru",
  "password": "1qa2ws3ed",
  "companies": [
    "GoodCompany"
  ]
}
```
* email обязателен
* companies список компаний в которых регистрируется пользователь

**Response**:
```
{
  "id": 2,
  "email": "test@test.ru",
  "companies": [
    "GoodCompany"
  ],
  "auth_company": null
}
```

## Авторизация
**POST /api/login/**
```
{
  "password": "1qa2ws3ed",
  "email": "test@test.ru",
  "auth_company": "GoodCompany"
}
```
**Response**
```
{
  "key": "27c47f07ed4a913fca1cb7fa5d9c9dae07f8a7e8"
}
```
**GET /api/logout/**
```
No parameters
```
**Response 200**
```
{}
```

## Профиль
Получить информацию о текущем пользователе.\
**GET /api/profile**
```
No parameters
```
**Response**
```
{
  "id": 2,
  "email": "test@test.ru",
  "companies": [
    "GoodCompany"
  ],
  "auth_company": "GoodCompany"
}
```

## TODO
Получить список.\
**GET /api/todos/**
```
No parameters 
```
**Response 200**
``` 
```

**POST /api/todos/**
```
{
  "description": "Do anything",
  "completed": false
} 
```

**Response**
``` 
{
    "id": 3,
    "company": {
        "id": 1,
        "name": "GoodCompany"
    },
    "description": "Do anything",
    "completed": false,
    "date_created": "2018-10-23T04:20:51.186441Z",
    "date_updated": "2018-10-23T04:20:51.186472Z"
}
```
Получить конкретный todo\
**GET /api/todos/{id}/**
``` 
```

**Response**
```
{
    "id": 3,
    "company": {
        "id": 1,
        "name": "GoodCompany"
    },
    "description": "Do anything",
    "completed": false,
    "date_created": "2018-10-23T04:20:51.186441Z",
    "date_updated": "2018-10-23T04:20:51.186472Z"
} 
```

Изменить конкретный todo\
**PATCH /api/todos/{id}/**
```
{
    "id": 3,
    "company": {
        "id": 1,
        "name": "GoodCompany"
    },
    "description": "Do anything",
    "completed": true,
    "date_created": "2018-10-23T04:20:51.186441Z",
    "date_updated": "2018-10-23T04:20:51.186472Z"
} 
```

**Response**
```
{
    "id": 3,
    "company": {
        "id": 1,
        "name": "GoodCompany"
    },
    "description": "Do anything",
    "completed": true,
    "date_created": "2018-10-23T04:20:51.186441Z",
    "date_updated": "2018-10-23T04:20:51.186472Z"
} 
```

Удалить конкртеный todo\
**DELETE /api/todos/{id}/**
