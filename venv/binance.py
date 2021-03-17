import os

from binance.client import Client
from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor

api_key = "WK8dITaZRDlJ2DRSjxZdrHbuvMRhSafCls8WdhGrmNArF3FoSxUmjlto3iTOvWDU"
api_secret = "acEjoqKOJ0TNlVYoZgDYrKVIYvStBfxAmCJG90rj3GYi7jlOJzwqqcAeLcLZN4BK"

client = Client(api_key, api_secret)


client.API_URL = 'https://testnet.binance.vision/api'
#print(client.get_asset_balance(asset='ETH'))
print(client.get_account())

try:
    order = client.create_order(
        symbol='ETHUSDT',
        side=Client.SIDE_BUY,
        type=Client.ORDER_TYPE_MARKET,
        quantity=1,
    )

except BinanceAPIException as e:
    # error handling goes here
    print(e)
except BinanceOrderException as e:
    # error handling goes here
    print(e)


print(order)



print(client.get_asset_balance(asset='ETH'))