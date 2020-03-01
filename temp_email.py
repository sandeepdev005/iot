import email_confy, json, time
from boltiot import Email, Bolt

minimum_limit = 300 
maximum_limit = 600

mybolt = Bolt(email_confy.API_KEY, email_confy.DEVICE_ID)
mailer = Email(email_confy.MAILGUN_API_KEY, email_confy.SANDBOX_URL, email_confy.SENDER_EMAIL, email_confy.RECIPIENT_EMAIL)
while True: 
    print ("Reading sensor value")
    response = mybolt.analogRead('A0') 
    data = json.loads(response) 
    print ("Sensor value is: " + str(data['value']))
    try: 
        sensor_value = int(data['value']) 
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
            print("Making request to Mailgun to send an email")
            response = mailer.send_email("Alert", "The Current temperature sensor value is " +str(sensor_value))
            response_text = json.loads(response.text)
            print("Response received from Mailgun is: " + str(response_text['message']))
    except Exception as e: 
        print ("Error occured: Below are the details")
        print (e)
    time.sleep(10)
