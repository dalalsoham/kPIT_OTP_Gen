from twilio.rest import Client
import random
# Your Twilio Account SID and Auth Token
account_sid = 'AC14bf1e53e20c5a64cd0dc790c14ec94b'
auth_token = '8acb5ea39b67d57de40bc9a99fd6a23f'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Phone number to send the OTP to
to_phone_number = '+919907524334'  # Replace with the specific phone number

# Generate OTP
otp = str(random.randint(1000, 9999))

# Message to be sent
message = f"Your OTP is: {otp}"

# Send SMS
client.messages.create(
    to=to_phone_number,
    from_='+12055649437',
    body=message
)
