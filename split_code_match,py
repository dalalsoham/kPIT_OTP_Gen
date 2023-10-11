import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def generate_random_code():
    # Generate 6 random digits
    code = ''.join(random.choice(string.digits) for _ in range(6))
    return code

# Generate a random code and store it in a variable
random_code = generate_random_code()

# Split the random code into two parts
first_part = random_code[:3]  # First 3 digits
second_part = random_code[3:]  # Last 3 digits

# Your email credentials
sender_email = "arijeetdas001@gmail.com"  # Your Gmail address
sender_password = "csts whga mkti lyxp"  # Your Gmail password
recipient_emails = ["arijeetdashotmail@gmail.com", "sdjack2826@gmail.com"]  # List of recipient's email addresses

# SMTP server settings
smtp_server = "smtp.gmail.com"
smtp_port = 465  # Use port 465 for SSL

# Connect to the SMTP server and send emails to each recipient
try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, sender_password)

        # Send the first part to the first recipient
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_emails[0]
        message["Subject"] = "Random Code Generated"
        body = f"Random Code: {first_part}"
        message.attach(MIMEText(body, "plain"))
        server.sendmail(sender_email, recipient_emails[0], message.as_string())
        print(f"Email sent to {recipient_emails[0]}")

        # Send the second part to the second recipient
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_emails[1]
        message["Subject"] = "Random Code Generated"
        body = f"Random Code: {second_part}"
        message.attach(MIMEText(body, "plain"))
        server.sendmail(sender_email, recipient_emails[1], message.as_string())
        print(f"Email sent to {recipient_emails[1]}")

    print("Emails sent successfully")

except Exception as e:
    print("Error sending emails:", e)

# Prompt the user for input
user_input = input("Enter the 6-digit code: ")

# Check if the input matches the stored random code
if user_input == random_code:
    print("Code matched")
else:
    print("Code mismatch has occurred")

# Print the original random code
print(f"Original Random Code: {random_code}")
