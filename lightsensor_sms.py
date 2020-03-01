import conf, json, time
from boltiot import Bolt, Sms

minimum_limit = 100
maximum_limit = 1000


myBolt = Bolt(conf.API_KEY,conf.DEVICE_ID)
sms = Sms(conf.SID,conf.AUTH_TOKEN,conf.TO_NUMBER,conf.FROM_NUMBER)

while True:
  print("Reading the LDR sensor value")
  response = myBolt.analogRead('A0')
  data = json.loads(response)
  sensor_value = int(data['value'])
  print("LDR sensor value is :" + str(data['value']))
  try:
    print("try block")
  except Exception as e:
    print("Exception")
