import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import hmac
import hashlib
import time

# Function to generate TOTP
def generate_totp(secret, time_step=30, length=6):
    current_time = int(time.time())
    counter = current_time // time_step
    hmac_digest = hmac.new(secret, counter.to_bytes(8, byteorder='big'), hashlib.sha1).digest()
    offset = hmac_digest[-1] & 0x0F
    binary_code = ((hmac_digest[offset] & 0x7F) << 24 |
                   (hmac_digest[offset + 1] & 0xFF) << 16 |
                   (hmac_digest[offset + 2] & 0xFF) << 8 |
                   (hmac_digest[offset + 3] & 0xFF))
    totp = str(binary_code % 10 ** length)
    return totp.zfill(length)

# Secret key used for TOTP
secret_key = b'Soham@2003'  # Replace with your secret key

# Generate TOTP
totp_code = generate_totp(secret_key)

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

        # Send the TOTP to the recipient's email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = "TOTP Generated"
        body = f"Your TOTP is: {totp_code}"
        message.attach(MIMEText(body, "plain"))
        server.sendmail(sender_email, recipient_email, message.as_string())
        print(f"TOTP sent to {recipient_email}")

except Exception as e:
    print("Error sending email:", e)

# Wait for user input
time.sleep(30)  # Wait for 30 seconds

# Prompt the user for input
user_input = input("Enter the 6-digit OTP: ")

# Check if the input matches the generated TOTP code
if user_input == totp_code:
    print("Code matched")
else:
    print("Code mismatch has occurred")

# Print the original TOTP code
print(f"Original TOTP Code: {totp_code}")
