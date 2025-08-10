#!/bin/sh
set -e

PORT=${PORT:-8080}

Запуск бота в фоне
python bot.py &
BOT_PID=$!

Простой health-check HTTP-сервер на порту 8080
python -m http.server "$PORT" --bind 0.0.0.0 &
HTTP_PID=$!

wait -n $BOT_PID $HTTP_PID
