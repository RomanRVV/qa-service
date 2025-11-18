# QA-backend 

Небольшой API-сервис для управления вопросами и ответами (Q&A) на Django и Django Ninja.

## Эндпоинты

Для вопросов:

- GET /questions/ — список всех вопросов

- POST /questions/ — создать новый вопрос

- GET /questions/{id} — получить вопрос и все ответы на него

- DELETE /questions/{id} — удалить вопрос (вместе с ответами)


Для ответов:

- POST /questions/{id}/answers/ — добавить ответ к вопросу

- GET /answers/{id} — получить конкретный ответ

- DELETE /answers/{id} — удалить ответ


## Запуск с помощью Docker

Скачайте и установите [docker](https://www.docker.com/)

Скачайте репозиторий к себе на сервер или на локальную машину
```sh
git clone https://github.com/RomanRVV/qa-service.git
```

Создайте .env файл в корне проекта, который содержит(для тестового запуска .env можно оставить пустым):

- `DJANGO__DEBUG` — дебаг-режим.
- `DJANGO__SECRET_KEY` — секретный ключ проекта.
- `DATABASE` — dns вашей postgres бд

Запустите команду из корня проекта:
```sh
docker compose up --build
```
Создайте тестового суперпользователя:
```sh
$ docker compose run --rm django python manage.py createsuperuser --no-input
```

В системе создастся суперпользователь:
- логин `admin`, пароль `admin`

База данных готова к работе.

Сайт доступен по адресу [127.0.0.1:8000](http://127.0.0.1:8000). Вход в админку находится по адресу [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

Для проверки работы API удобно использовать Swagger UI, который находится по адресу [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs).

Тесты прогоняются при сборке, но можно и отдельной командой:
```sh
docker compose run --rm tests
```
