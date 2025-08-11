from aiogram import types
from utils.db import add_user, set_price_alert
from services.price import get_top_10_prices
from services.gas import get_gas_price
from services.drops import get_nft_drops
import json

from utils.telegram_bot import dp

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    add_user(message.from_user.id, message.from_user.username)
    await message.answer("👋 Привет! Я — CryptoPulse. Отслеживаю цены, газ, NFT и китов.\n\n"
                         "Команды:\n"
                         "/price — топ-10 монет\n"
                         "/gas — газ на Ethereum\n"
                         "/drops — NFT-дропы\n"
                         "/alert 3000 — алерт при падении ETH ниже $3000")

@dp.message_handler(commands=['price'])
async def cmd_price(message: types.Message):
    prices = get_top_10_prices()
    text = "📊 Топ-10 криптовалют:\n\n"
    for p in prices:
        text += f"🟢 {p['name']} (${p['symbol']})\n"
        text += f"Цена: ${p['price']:,}\n"
        text += f"Изм: {p['change_24h']:+.2f}%\n\n"
    await message.answer(text)

@dp.message_handler(commands=['gas'])
async def cmd_gas(message: types.Message):
    gas = get_gas_price()
    text = "⛽️ Газ (Gwei):\n"
    text += f"🐢 Медленно: {gas['safe']}\n"
    text += f"🐇 Средне: {gas['propose']}\n"
    text += f"⚡️ Быстро: {gas['fast']}"
    await message.answer(text)

@dp.message_handler(commands=['drops'])
async def cmd_drops(message: types.Message):
    drops = get_nft_drops()
    text = "🔥 NFT Дропы:\n\n"
    for d in drops:
        text += f"🎨 {d['name']}\n"
        text += f"📅 {d['date']}\n"
        text += f"⛓️ {d['chain']}\n"
        text += f"💰 {d['price']}\n"
        text += f"🔗 {d['link']}\n\n"
    await message.answer(text)

@dp.message_handler(commands=['alert'])
async def cmd_alert(message: types.Message):
    try:
        price = float(message.get_args())
        set_price_alert(message.from_user.id, price)
        await message.answer(f"✅ Алерт установлен: ETH < ${price}")
    except:
        await message.answer("Используй: /alert 3000")