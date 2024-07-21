# Ledmi
Rental+video gallery created with django, docker, postgres, celery+rabbitmq, gunicorn and nginx. Adaptive and cross browser. 

<p align="center">
  <img width="500" height="500" src="https://github.com/user-attachments/assets/09219dc3-89b4-4921-a077-2b42a7ad1785">
</p>            


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
3. Для управления панелью администратора создайте суперпользователя
   
   ```sh
    docker-compose exec web python manage.py createsuperuser
   ```

4. Для доступа к панели управления nginx активируйте соответствующий плагин

    ```sh
    docker-compose exec rabbitmq rabbitmq-plugins enable rabbitmq_management
    ```

5. Откройте браузер и перейдите по адресу:

    ```
    http://127.0.0.1:8000
    ```
