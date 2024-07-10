# Используем официальный образ Python в качестве базового
FROM python:3.10-slim

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /Rental

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt /Rental/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в рабочую директорию
COPY . /Rental/

# Указываем порт, который будет использоваться
EXPOSE 8000

# Команда для запуска контейнера
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Rental.wsgi:application"]