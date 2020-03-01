from boltiot import Bolt
api_key="468b7098-505b-4d74-b955-faa4c2f1cb30"
device_id="BOLT292292"
myBolt = Bolt(api_key,device_id)
response = myBolt.analogWrite('0','10')
print(response)

