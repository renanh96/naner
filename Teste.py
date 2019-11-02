from API1_a import a
from API2_b import b
import time


while True:
    var1 = a['asks'][0]['price']
    var2 = b['data']['asks'][0]['unit_price']
    if var1 > var2:
        print('A (', var1, ') maior que B (', var2, ')')
        time.sleep(2)
    else:
        print('A (', var1, ') menor que B (', var2, ')')
        time.sleep(2)