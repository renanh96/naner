from time import time
import requests
import json
import urllib.parse
import hashlib
import hmac

APIkey = b'9c9d84162ea26a1da642324c5208dde59a30b02b5a37db688b0d2e6faba8ba9078f23ea3c4f65400fdae33554ae151de5696a7c1e017b3e41a77d5a740b6e309'
secret = b'37d5b8505b5e65d18aa6c11a2da108cdd4894ee3c0c80e9592ccbddc1b11ffb8b5d0c52fb3f78f034952600b4fb4ca3a44219fcd8e435ea1de05afe6f0abbfa3'
payload = {'nonce': int(time() * 1000)}

paybytes = urllib.parse.urlencode(payload).encode('utf8')
sign = hmac.new(secret, paybytes, hashlib.sha512).hexdigest()
headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Key': APIkey, 'Sign': sign}

####################### Ver as melhores ofertas no livro ###############################
# pares de moedas >> ltc_btc, eth_btc, dash_btc, eth_brl, btc_brl, eth_brl
r = requests.get('https://braziliex.com/api/v1/public/orderbook/btc_brl', headers=headers, data=paybytes)
a = json.loads(r.text)

#print('')
#print('#### A 1ª MELHOR OPÇÃO DE VENDA ####')
#print('Preço unitário:', braziliex_ordem['asks'][0]['price'])
#print('Em bitcoin:', braziliex_ordem['asks'][0]['amount'])
#print('')
#print('#### A 2ª MELHOR OPÇÃO DE VENDA ####')
#print('Preço unitário:', braziliex_ordem['asks'][1]['price'])
#print('Em bitcoin:', braziliex_ordem['asks'][1]['amount'])
#print('')
#print('#### A 1ª MELHOR OPÇÃO DE COMPRA ####')
#print('Preço unitário: ', braziliex_ordem['bids'][0]['price'])
#print('Em bitcoin:', braziliex_ordem['bids'][0]['amount'])
#print('')
#print('#### A 2ª MELHOR OPÇÃO DE COMPRA ####')
#print('Preço unitário: ', braziliex_ordem['bids'][1]['price'])
#print('Em bitcoin:', braziliex_ordem['bids'][1]['amount'])