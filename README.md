# Ledmi
Rental created with django, docker, postgres, celery+rabbitmq, gunicorn and nginx. Adaptive and cross browser.

## Требования

- Python 3.x
- pip
- virtualenv

## Установка

1. Переименуйте файл .env.example в .env и отредактируйте, если хотите настроить проект под себя.

2. Постройте и запустите контейнеры:

    ```sh
    docker-compose up --build
    ``` 

2. Откройте браузер и перейдите по адресу:

    ```
    http://127.0.0.1:8000
    ```
