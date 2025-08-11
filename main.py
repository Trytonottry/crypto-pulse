from utils.telegram_bot import dp, bot
from utils.db import init_db
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from flask import Flask
import asyncio
import threading

# Инициализация
init_db()

# Flask
app = Flask(__name__)
from web.views import web
app.register_blueprint(web)

def run_web():
    app.run(host="127.0.0.1", port=5000, debug=False)

# Запуск веба в отдельном потоке
web_thread = threading.Thread(target=run_web)
web_thread.start()

# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)