# KinkyHub Bot — инструкция по Railway (мобильно)

Цель: запуск Telegram-бота 24/7 через Railway. Токен хранится как переменная окружения BOT_TOKEN. Медиа в папке media. Логи кликов в stats.txt. Поддержка UA и EN.

## Что внутри
- bot.py — основной код (мультиязычность, автоподогрев, кнопки и логика)
- media/
  - day0.jpg
  - day2.jpg
  - day4.jpg
- requirements.txt
- Procfile
- stats.txt — лог кликов (создается автоматически)
- README.md — инструкция (этот файл)

## Как запустить на Railway (мобильно)
1) Создать приватный репозиторий kinkyhub-bot на GitHub и загрузить файлы (bot.py, media, requirements.txt, Procfile).
2) В Railway: New Project → Deploy from GitHub Repo → выбрать kinkyhub-bot → Deploy.
3) В Settings → Variables → Add Variable:
   - BOT_TOKEN: ваш токен
4) Дождаться лога: ✅ BOT STARTED
5) Протестировать через Telegram: подать заявку и проверить приветствие/кнопки.

## Как менять контент
- Медиа: media/day0.jpg, day2.jpg, day4.jpg — заменяй своими файлами с теми же именами.
- Тексты: правь внутри bot.py в блоке MESSAGES (ua/en).
- Ссылки: CHAT_LINKS в коде — замени на свои.

## Как смотреть аналитику
- При клике кнопки бот записывает строку в stats.txt: дата | user_id | name | button

## Что дальше
- Могу добавить автосообщения на Day 1 и Day 3, добавить клики по кнопкам в виде аналитики и т.д.