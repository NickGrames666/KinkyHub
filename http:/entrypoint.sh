#!/bin/sh
set -e

# Запускаем бота в фоновом режиме
python bot.py &
BOT_PID=$!

# Делаем простой Health-Check HTTP-сервер на порту 8080
# Этот сервер просто отвечает 200 на любой GET
python -m http.server 8080 --bind 0.0.0.0 &
HTTP_PID=$!

# Ожидаем завершения любого процесса
wait -n $BOT_PID $HTTP_PID
