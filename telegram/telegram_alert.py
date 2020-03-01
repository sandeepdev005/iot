import requests
import json
import time
from boltiot import Bolt
import conf

mybolt = Bolt(conf.bolt_api_key,conf.device_id)

def get_sensor_value_from_pin(pin):
     try:
       response = mybolt.analogRead(pin)
       data = json.loads(response)
       if data["success"] != 1:
          print("Request Failed")
          print("This is a response->",data)
          return -999
       sensor_value = int(data['value'])
       return sensor_value
     except Exception as e:
       print("some thing went wrong")
       print(e)
       return -999


def send_telegram_message(message):
    """Sends message via Telegram"""
    url = "https://api.telegram.org/" + conf.telegram_bot_id + "/sendMessage"
    data = {
        "chat_id": conf.telegram_chat_id,
        "text": message
    }
    try:
        response = requests.request(
            "POST",
            url,
            params=data
        )
        print("This is the Telegram response")
        print(response.text)
        telegram_data = json.loads(response.text)
        return telegram_data["ok"]
    except Exception as e:
        print("An error occurred in sending the alert message via Telegram")
        print(e)
        return False



while True:
     # sensor_value = get_sensor_value_from_pin("A0")
     sensor_value = get_sensor_value_from_pin("A0")
     print("The current sensor value is :", sensor_value)
     
     if sensor_value == -999:
        print("Request was unsuccessfull. Skipping")
        time.sleep(10)
        continue

     if sensor_value >= conf.threshold:
        print("Sensor value has exceeded threshold")
        message = "Alert! Sensor value has exceeded" + str(conf.threshold) +"The current value is "+ str(sensor_value)
        telegram_status = send_telegram_message(message)
        print("this is the telegram status:",telegram_status)

     time.sleep(10)  
