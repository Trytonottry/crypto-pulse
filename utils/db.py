import sqlite3

def init_db():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            alert_price REAL
        )
    ''')
    conn.commit()
    conn.close()

def add_user(user_id, username):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)', (user_id, username))
    conn.commit()
    conn.close()

def set_price_alert(user_id, price):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('UPDATE users SET alert_price = ? WHERE user_id = ?', (price, user_id))
    conn.commit()
    conn.close()