from flask import Blueprint, render_template
from services.price import get_top_10_prices
from services.drops import get_nft_drops

web = Blueprint('web', __name__)

@web.route('/')
def index():
    prices = get_top_10_prices()
    return render_template('index.html', prices=prices)

@web.route('/drops')
def drops():
    drops_list = get_nft_drops()
    return render_template('drops.html', drops=drops_list)