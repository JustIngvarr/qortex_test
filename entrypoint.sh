#!/bin/sh

echo "Миграция..."
python manage.py migrate
echo ""

echo "Создаем суперпользователя, если его нет..."
echo "from django.contrib.auth import get_user_model; User=get_user_model(); \
import sys; User.objects.filter(username='admin').exists() or \
User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" | python manage.py shell

echo "Собираем статику..."
python manage.py collectstatic --noinput
echo ""

echo "Добавим данных в БД..."
python manage.py loaddata music.json
echo ""

echo "Запускаем сервер..."
exec "$@"
