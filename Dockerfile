# Python
FROM python:3.10-slim

# Настройка переменных окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости для psycopg2 и других пакетов
RUN apt update && apt install -y libpq-dev gcc && apt clean

# Создаём рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt /app/

# Устанавливаем зависимости Python
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . /app/

# Делаем entrypoint.sh исполняемым
RUN chmod +x /app/entrypoint.sh

# Запускаем команду по умолчанию
ENTRYPOINT ["/app/entrypoint.sh"]
