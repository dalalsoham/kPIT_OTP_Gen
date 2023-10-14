from twilio.rest import Client

account_sid = 'AC14bf1e53e20c5a64cd0dc790c14ec94b'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+12055649437',
  to='+919907524334'
)

print(message.sid)