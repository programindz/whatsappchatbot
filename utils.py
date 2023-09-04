from twilio.rest import Client
import os 

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)



def send_message(number, text):
  try:
    message = client.messages.create(
      from_='whatsapp:+14155238886',
      body=f"{text}",
      to=f"whatsapp:{number}"
      )
  except Exception as e:
    print("Exception: ", e)
