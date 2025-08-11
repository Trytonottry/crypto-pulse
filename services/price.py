import requests

def get_top_10_prices():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1
    }
    r = requests.get(url, params=params)
    coins = r.json()
    result = []
    for c in coins:
        result.append({
            'name': c['name'],
            'symbol': c['symbol'].upper(),
            'price': c['current_price'],
            'change_24h': c['price_change_percentage_24h']
        })
    return result