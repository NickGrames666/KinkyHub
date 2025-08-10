import os
import asyncio
import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, CallbackQueryHandler, ContextTypes

# Берём токен из переменной окружения BOT_TOKEN
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ===== НАСТРОЙКИ =====

MEDIA_FILES = {
    "day0": "media/day0.jpg",  # Приветствие
    "day2": "media/day2.jpg",  # Через 2 дня
    "day4": "media/day4.jpg",  # Через 4 дня
}

CHAT_LINKS = {
    "main_chat": "https://t.me/+novjZfOZW9ozYTAy",  # Основной Кинки Хаб
    "escort": "https://t.me/+lFxPJhQwd4U3YzYy",    # Вирт услуги / эскорт
    "ua_chat": "https://t.me/golosovoy_chats_ukraina"  # Чат Украина
}

MESSAGES = {
    "ua": {
        "welcome": (
            "🔥 Привіт, {name}!\n"
            "Ти подав заявку до **KinkyHub** — місця, де 🔞 моделі продають нюдси та роблять приват відеодзвінки.\n\n"
            "💎 Що на тебе чекає:\n"
            "💋 Ексклюзивні фото та відео без цензури\n"
            "🖤 Приват-стріми прямо в Telegram\n"
            "✨ Реальне спілкування з моделями\n\n"
            "⚡ Натисни, доки доступ відкритий 👇"
        ),
        "day2": (
            "😈 Подивись, що з'явилося сьогодні:\n"
            "📸 Нові фото та приват від моделей\n"
            "🎥 Гарячі відео 18+\n"
            "🔓 Усе це в **KinkyHub**\n\n"
            "👉 Заходь зараз: {main}"
        ),
        "day4": (
            "⏳ {name}, твій пропуск у **KinkyHub** скоро закриється!\n\n"
            "Не пропусти:\n"
            "💋 доступ до приватів\n"
            "📸 ексклюзивні фото\n"
            "💻 приват-чати з моделями\n\n"
            "👉 Устигни: {main}"
        )
    },
    "en": {
        "welcome": (
            "🔥 Hi, {name}!\n"
            "You applied to **KinkyHub** — the place where 🔞 models sell nudes and do private video calls.\n\n"
            "💎 What awaits you:\n"
            "💋 Exclusive uncensored photos & videos\n"
            "🖤 Private streams right in Telegram\n"
            "✨ Real chats with models\n\n"
            "⚡ Tap while access is open 👇"
        ),
        "day2": (
            "😈 Look what’s new today:\n"
            "📸 New photos & private shows from models\n"
            "🎥 Hot 18+ videos\n"
            "🔓 All this is in **KinkyHub**\n\n"
            "👉 Join now: {main}"
        ),
        "day4": (
            "⏳ {name}, your pass to **KinkyHub** is closing soon!\n\n"
            "Don't miss:\n"
            "💋 access to privates\n"
            "📸 exclusive photos\n"
            "💻 private chats with models\n\n"
            "👉 Hurry: {main}"
        )
    }
}

# ===== ФУНКЦИИ =====

def get_keyboard(lang="ua"):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔥 KinkyHub", callback_data="main_chat")],
        [InlineKeyboardButton("💌 Вірт / Escort", callback_data="escort")],
        [InlineKeyboardButton("📢 Чат Україна", callback_data="ua_chat")],
    ])

async def send_delayed_messages(bot, user_id, name, lang):
    # День 2 — через 2 дня
    await asyncio.sleep(2 * 86400)
    try:
        await bot.send_photo(
            chat_id=user_id,
            photo=open(MEDIA_FILES["day2"], "rb"),
            caption=MESSAGES[lang]["day2"].format(main=CHAT_LINKS["main_chat"]),
            parse_mode="Markdown"
        )
    except:
        pass

    # День 4 — через 2 дня (итого 4 дня)
    await asyncio.sleep(2 * 86400)
    try:
        await bot.send_photo(
            chat_id=user_id,
            photo=open(MEDIA_FILES["day4"], "rb"),
            caption=MESSAGES[lang]["day4"].format(name=name, main=CHAT_LINKS["main_chat"]),
            parse_mode="Markdown"
        )
    except:
        pass

async def join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    lang_code = "ua" if (user.language_code and user.language_code.startswith("uk")) else "en"

    try:
        await context.bot.send_photo(
            chat_id=user.id,
            photo=open(MEDIA_FILES["day0"], "rb"),
            caption=MESSAGES[lang_code]["welcome"].format(name=user.first_name),
            parse_mode="Markdown",
            reply_markup=get_keyboard(lang_code)
        )
        asyncio.create_task(send_delayed_messages(context.bot, user.id, user.first_name, lang_code))
    except:
        print(f"⚠️ Не удалось отправить {user.first_name}")

    await update.chat_join_request.approve()

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = query.from_user
    button_id = query.data

    # Логируем клики
    with open("stats.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} | {user.id} | {user.first_name} | {button_id}\n")

    await query.answer()
    await context.bot.send_message(chat_id=user.id, text=f"🔗 {CHAT_LINKS[button_id]}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(join_request))
    app.add_handler(CallbackQueryHandler(button_click))
    print("✅ BOT STARTED")
    app.run_polling()

if __name__ == "__main__":
    main()