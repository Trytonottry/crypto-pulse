import requests

def get_gas_price():
    url = "https://api.etherscan.io/api"
    params = {
        'module': 'gastracker',
        'action': 'gasoracle',
        'apikey': 'YOUR_ETHERSCAN_KEY'
    }
    r = requests.get(url, params=params)
    data = r.json()['result']
    return {
        'safe': data['SafeGasPrice'],
        'propose': data['ProposeGasPrice'],
        'fast': data['FastGasPrice']
    }