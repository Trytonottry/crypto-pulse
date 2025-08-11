# CryptoPulse 💎 — Web3 Monitoring System

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![Framework](https://img.shields.io/badge/Framework-Aiogram%20%2B%20Flask-orange)
![Status](https://img.shields.io/badge/status-Production%20Ready-brightgreen)
[![Telegram](https://img.shields.io/badge/Chat-Telegram-blue?logo=telegram)](https://t.me/moriartyyyyy)

> 🚀 Полноценный Telegram-бот + веб-интерфейс для отслеживания цен, NFT-дропов, газа и алертов в реальном времени.  
> Идеально подходит для перепродажи, кастомизации или обучения.

---

## ✨ Функции

- 💰 **Цены топ-10 монет** (CoinGecko API)
- ⛽ **Газовые цены** (Ethereum, Polygon)
- 🎨 **NFT Drops Calendar** — ближайшие минты
- 🔔 **Пользовательские алерты** (например: "Сообщи, если ETH < $3000")
- 🌐 **Веб-интерфейс** (Flask + HTML/CSS)
- 📊 **SQLite-база** для хранения пользователей и настроек
- 🔄 **Автоматическая рассылка** каждые 5 минут
- 📦 **Готов к продаже** — как цифровой продукт

---

## 🛠 Технологии

- `Python 3.8+`
- `aiogram` — Telegram-бот
- `Flask` — веб-интерфейс
- `requests` — API-вызовы
- `APScheduler` — фоновые задачи
- `SQLite` — локальная база данных

---

## 📦 Установка

1. Склонируй репозиторий:
   ```bash
   git clone https://github.com/Trytonottry/cryptopulse.git
   cd cryptopulse
   ```
2. Установи зависимости: 
```bash
pip install -r requirements.txt
```
 
3. Настрой конфиг: 
```bash
cp config.example.py config.py
```
 
4. Открой config.py и вставь свои ключи: 

    TELEGRAM_BOT_TOKEN — получи от @BotFather 
    ETHERSCAN_API_KEY — регистрация на Etherscan 
     

5. Запусти: 
```bash
python main.py
```  
     
💡 Бот и веб-интерфейс запустятся автоматически.
Веб: http://127.0.0.1:5000  
     

## 🧪 Доступные команды 

/start - Приветствие
/price - Топ-10 монет
/gas - Газовые цены
/drops - NFT-дропы
/alert 3000 - Алерт при падении ETH ниже $3000
 
## 💬 Поддержка 

Если нужна помощь — пиши в Telegram: @moriartyyyyy 
Готов помочь с настройкой, хостингом и кастомизацией. 