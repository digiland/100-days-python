# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


SID = "AC6ca448808272c59bd8cdbf0d8c367c52"
AUTH_TOKEN = "b32f8209cd7d73b0b29426a2d13cf0c7"
MY_Number = "+18646354721"

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                    from_='+15017122661',
                    to='+15558675310'
                )

print(message.sid)
