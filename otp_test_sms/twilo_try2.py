import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from twilio.rest import Client  # Import the Twilio library

# Function to generate a random code
def generate_random_code():
    characters = string.digits + string.ascii_uppercase
    code = ''.join(random.choice(characters) for _ in range(6))
    return code

# Generate a random code
random_code = generate_random_code()

# Split the random code into two parts
first_part = random_code[:3]
second_part = random_code[3:]

# Your email credentials and Twilio credentials
sender_email = "arijeetdas001@gmail.com"
sender_password = "csts whga mkti lyxp"
recipient_email = "arijeetdashotmail@gmail.com"
twilio_account_sid = "AC14bf1e53e20c5a64cd0dc790c14ec94b"
twilio_auth_token = "8acb5ea39b67d57de40bc9a99fd6a23f"
twilio_phone_number = "your_twilio_phone_number"
recipient_phone_number = "+917364046052"  # Replace with the recipient's phone number

# SMTP server settings
smtp_server = "smtp.gmail.com"
smtp_port = 465

# Connect to the SMTP server and send emails to the recipient
try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, sender_password)

        # Send the first part to the recipient's email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = "Random Code Generated"
        body = f"Random Code: {first_part}"
        message.attach(MIMEText(body, "plain"))
        server.sendmail(sender_email, recipient_email, message.as_string())
        print(f"Email sent to {recipient_email}")

    print("Email sent successfully")

except Exception as e:
    print("Error sending email:", e)

# Use Twilio to send the second part (last 3 digits) as an OTP to the phone number
try:
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        to=recipient_phone_number,
        from_=twilio_phone_number,
        body=f"Your OTP is: {second_part}"
    )
    print(f"OTP sent to {recipient_phone_number}")

except Exception as e:
    print("Error sending OTP:", e)

# Prompt the user for input
user_input = input("Enter the 6-character alphanumeric code: ")

# Check if the input matches the stored random code
if user_input == random_code:
    print("Code matched")
else:
    print("Code mismatch has occurred")

# Print the original random code
print(f"Original Random Code: {random_code}")