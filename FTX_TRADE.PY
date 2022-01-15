from config import FTX_API_KEY,FTX_API_SECRET
import ccxt
import pandas as pd

ftx = ccxt.ftx({
 'api_key': FTX_API_KEY, # API Keys
 'secret': FTX_API_SECRET}) # API Secret

ftx.fetch_balance()

