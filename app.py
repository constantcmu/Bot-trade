
import json
from flask import Flask , request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/webhook")
def webhook():
    return "This is url for webhook!"

@app.route("/signals",methods=['POST'])
def signals():
    print("Someone Post Signals to me!")
    signal = request.data.decode("utf-8")
    signal = json.loads(signal)

    trade_size = signal["ACTION"]
    amount_coin = float(signal["AMOUNT_COIN"])
    leverage = int(signal["LEV"])
    symbol = signal["SYMBOL"]

    print("signal is")
    print(trade_size)
    print(amount_coin)
    print(leverage)
    print(symbol)
    print("บอททำคำสั่งไป Binance")

    message = f"ได้รับสัญญาณการซื้อขาย ดันงนี้ .... \n{trade_size} {symbol} \nจำนวนที่เปิด {amount_coin} \nLEVERAGE {leverage}"
    from line_notify import LineNotify

    ACCESS_TOKEN = "SUTUl3GEBKeM8hzeuCImz8vp0b8bQnxF8dDJV76UMhh"

    notify = LineNotify(ACCESS_TOKEN)

    notify.send(message)


    return "200" #ถ้าโอเคจะส่งตัวเลข 200 


if __name__=="__main__":
    app.run()