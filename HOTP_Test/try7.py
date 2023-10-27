import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import hmac
import hashlib
import time
import secrets
import string

# Function to generate Alphanumeric OTP
def generate_alphanumeric_otp(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

# Secret key used for TOTP
secret_key = b'Soham@2003'  # Replace with your secret key

# Generate Alphanumeric OTP
totp_code = generate_alphanumeric_otp()

# Your email credentials
sender_email = "sdjack2826@gmail.com"
sender_password = "auxg xfnh recc ohzz"
recipient_email = "barson0habra@gmail.com"

smtp_server = "smtp.gmail.com"
smtp_port = 465

# Connect to the SMTP server and send email to the recipient
try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, sender_password)

        # Send the OTP to the recipient's email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = "Alphanumeric OTP Generated"
        body = f"Your Alphanumeric OTP is: {totp_code}"
        message.attach(MIMEText(body, "plain"))
        server.sendmail(sender_email, recipient_email, message.as_string())
        print(f"Alphanumeric OTP sent to {recipient_email}")

except Exception as e:
    print("Error sending email:", e)

# Prompt the user for input with a timeout of 60 seconds
start_time = time.time()
timeout = 60
elapsed_time = 0
code_matched = False

while elapsed_time < timeout:
    user_input = input(f"Enter the {len(totp_code)}-character Alphanumeric OTP ({int(timeout - elapsed_time)} seconds remaining): ")

    if user_input == totp_code:
        code_matched = True
        print("Code matched")
        break

    elapsed_time = time.time() - start_time

if elapsed_time >= timeout:
    print("Timeout. You did not enter the OTP in time.")

if code_matched and elapsed_time >= timeout:
    print("You entered the correct code after timeout.")
