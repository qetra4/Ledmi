# Ledmi
Rental created with django, docker, postgres, celery+rabbitmq, gunicorn and nginx. Adaptive and cross browser.

## Требования

- Python 3.x
- pip
- virtualenv

## Установка

1. Склонируйте репозиторий:

    ```sh
    git clone https://github.com/qetra4/ledmi.git
    cd ledmi
    ```

2. Создайте виртуальное окружение и активируйте его:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```

3. Установите зависимости:

    ```sh
    pip install -r requirements.txt
    ```

4. Создайте файл `.env` на основе примера:

    ```sh
    cp .env.example .env
    ```

    Отредактируйте файл `.env` и укажите необходимые переменные окружения.

5. Примените миграции базы данных:

    ```sh
    python manage.py migrate
    ```

6. Соберите статические файлы (если необходимо):

    ```sh
    python manage.py collectstatic
    ```

7. Запустите сервер разработки:

    ```sh
    python manage.py runserver
    ```

## Docker (опционально)

Если вы используете Docker, вы можете запустить проект следующим образом:

1. Постройте и запустите контейнеры:

    ```sh
    docker-compose up --build
    ```

2. Откройте браузер и перейдите по адресу:

    ```
    http://127.0.0.1:8000
    ```

## Примечания

- Убедитесь, что файл `requirements.txt` содержит все зависимости вашего проекта.
- Убедитесь, что файл `.env.example` содержит все необходимые переменные окружения и инструкции по их заполнению.
