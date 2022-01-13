import json
import requests

url = 'http://127.0.0.1:5000/signals'
msg = {
            'ACTION': 'OPEN LONG',
            'AMOUNT_COIN': '0.01',
            'LEV': '30',
            'SYMBOL': 'BTCBUSD',
        }

msg = json.dumps(msg)

x = requests.post(url, data = msg)

print(x.text)