import requests
import json

            #Ver as ordens ativas no book
bitcointrade_orders = requests.get('https://api.bitcointrade.com.br/v2/public/BRLBTC/orders')

b = json.loads(bitcointrade_orders.text)
#print('')
#print('#### A 1ª MELHOR OPÇÃO DE COMPRA ####')
#print('Valor unitário de compra:', bitcointrade_orders_book['data']['bids'][0]['unit_price'])
#print('Conversão em Bitcoin:', bitcointrade_orders_book['data']['bids'][0]['amount'])
#print('')
#print('#### A 2ª MELHOR OPÇÃO DE COMPRA ####')
#print('Valor unitário de compra:', bitcointrade_orders_book['data']['bids'][1]['unit_price'])
#print('Conversão em Bitcoin:', bitcointrade_orders_book['data']['bids'][1]['amount'])
#print('')
            #Ver as ordes ativas no book de venda
#print('#### A 1ª MELHOR OPÇÃO DE VENDA ####')
#print('Valor unitário de de venda:', bitcointrade_orders_book['data']['asks'][0]['unit_price'])
#print('Conversão em Bitcoin:', bitcointrade_orders_book['data']['asks'][0]['amount'])
#print('')
#print('#### A 2ª MELHOR OPÇÃO DE VENDA ####')
#print('Valor unitário de venda:', bitcointrade_orders_book['data']['asks'][1]['unit_price'])
#print('Conversão em Bitcoin:', bitcointrade_orders_book['data']['asks'][1]['amount'])