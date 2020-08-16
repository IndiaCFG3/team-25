from twilio.rest import Client

# Setup
#npm install twilio-cli -g
#pip install twilio

account_sid = 'ACfa5a6384a294f1a8385481fece3f964a'
auth_token = 'f0bab8e671bbb9ab68e2ab84417b1e04'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Test Message",
                     from_='+12058585073',
                     to=''  # Recivers number with +91
                 )

print(message.sid)
