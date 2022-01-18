
import json
import requests

url = 'http://127.0.0.1:5000/signals'
heroku_url = "https://immense-retreat-47353.herokuapp.com/signals"
msg = {
            'ACTION': 'TPSL LONG',
            'AMOUNT_COIN': '0.04',
            'LEV': '0',
            'SYMBOL': 'BNBBUSD',
        }

msg = json.dumps(msg)

x = requests.post(heroku_url, data = msg)

print(x.text)  