import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import hmac
import hashlib

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

# Secret key used for HOTP
secret_key = b'My name is SOHAM dalal'  # Replace with your secret key

# Generate a counter (you can use a time-based counter in practice)
counter = 1

# Generate HOTP
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

        # Send the HOTP to the recipient's email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = "HOTP Generated"
        body = f"Your HOTP is: {hotp_code}"
        message.attach(MIMEText(body, "plain"))
        server.sendmail(sender_email, recipient_email, message.as_string())
        print(f"HOTP sent to {recipient_email}")

except Exception as e:
    print("Error sending email:", e)

# Prompt the user for input
user_input = input("Enter the 6-digit OTP: ")

# Check if the input matches the generated HOTP code
if user_input == hotp_code:
    print("Code matched")
else:
    print("Code mismatch has occurred")

# Print the original HOTP code
print(f"Original HOTP Code: {hotp_code}")
