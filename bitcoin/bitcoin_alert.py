import requests
import json
import time
from boltiot import Bolt


def get_bitcoin_price():
    URL="https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,INR"
    response = requests.request("GET",URL)
    response = json.loads(response.text)
    current_price = response["USD"]
    return current_price

sellingPrice = 7435.15
while True:
 print("bitcoin price", get_bitcoin_price())
 bitcoin_price = get_bitcoin_price()
 if sellingPrice < bitcoin_price :
   mybolt= Bolt("468b7098-505b-4d74-b955-faa4c2f1cb30","BOLT292292")
   response = mybolt.digitalWrite('0','HIGH')
   time.sleep(3)
   response = mybolt.digitalWrite('0','LOW')
   print(response)
 time.sleep(30)
