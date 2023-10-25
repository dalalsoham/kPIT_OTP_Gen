import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def generate_random_code():
    # Generate 3 random letters
    letters = ''.join(random.choice(string.ascii_letters) for _ in range(3))

    # Generate 3 random digits
    digits = ''.join(random.choice(string.digits) for _ in range(3))

    # Combine and shuffle the characters
    code = ''.join(random.sample(letters + digits, 6))
    
    return code

# Example: Generate a 6-digit code with 3 letters and 3 digits
random_code = generate_random_code()
print(random_code)


# Your email credentials
sender_email = "arijeetdas001@gmail.com"  # Your Gmail address
sender_password = "csts whga mkti lyxp"  # Your Gmail password
recipient_email = "arijeetdashotmail@gmail.com"  # Recipient's email address

# SMTP server settings
smtp_server = "smtp.gmail.com"
smtp_port = 465  # Use port 465 for SSL

# Create the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = "Random Code Generated"
body = f"Random Code: {random_code}"
message.attach(MIMEText(body, "plain"))

# Connect to the SMTP server and send the email
try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
    print("Email sent successfully")
except Exception as e:
    print("Error sending email:", e)

print(f"Random Code: {random_code}")