FROM python:3.11-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё
COPY . .

# Делать файл исполняемым (на случай, если используем entrypoint)
RUN chmod +x entrypoint.sh

# Открываем порт, который будет использовать http-сервер
EXPOSE 8080

# Запуск: запускаем бота в фоне и запускаем простой HTTP-сервер для health-check
CMD ["./entrypoint.sh"]
