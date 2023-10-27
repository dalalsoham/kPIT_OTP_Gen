import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import hmac
import hashlib
import time

# Function to generate HOTP
def generate_hotp(secret, counter, length=6):
    hmac_digest = hmac.new(secret, counter.to_bytes(8, byteorder='big'), hashlib.sha1).digest()
    offset = hmac_digest[-1] & 0x0F
    binary_code = ((hmac_digest[offset] & 0x7F) << 24 |
                   (hmac_digest[offset + 1] & 0xFF) << 16 |
                   (hmac_digest[offset + 2] & 0xFF) << 8 |
                   (hmac_digest[offset + 3] & 0xFF))
    hotp = str(binary_code % 10 ** length)
    return hotp.zfill(length)

# Function to generate TOTP
def generate_totp(secret, time_step=30, length=6):
    current_time = int(time.time())
    counter = current_time // time_step
    return generate_hotp(secret, counter, length)

# Secret key used for TOTP and HOTP
secret_key = b'Soham@2003'  # Replace with your secret key

# Generate TOTP
totp_code = generate_totp(secret_key)

# Generate HOTP (for demonstration purposes, increment the counter)
counter = 1
hotp_code = generate_hotp(secret_key, counter)

# Your email credentials
sender_email = "sdjack2826@gmail.com"
sender_password = "auxg xfnh recc ohzz"
recipient_email = "barson0habra@gmail.com"

smtp_server = "smtp.gmail.com"
smtp_port = 465

# Connect to the SMTP server and send emails to the recipient
try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, sender_password)

        # Send the TOTP and HOTP to the recipient's email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = "Mixed OTP Generated"
        body = f"Your TOTP is: {totp_code}\nYour HOTP is: {hotp_code}"
        message.attach(MIMEText(body, "plain"))
        server.sendmail(sender_email, recipient_email, message.as_string())
        print(f"OTP sent to {recipient_email}")

except Exception as e:
    print("Error sending email:", e)

# Prompt the user for input
user_input = input("Enter the 6-digit OTP: ")

# Check if the input matches the generated OTP codes
if user_input == totp_code or user_input == hotp_code:
    print("Code matched")
else:
    print("Code mismatch has occurred")

# Print the original OTP codes
print(f"Original TOTP Code: {totp_code}")
print(f"Original HOTP Code: {hotp_code}")
