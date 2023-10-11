import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def generate_random_digit():
    return str(random.randint(0, 9))

# Generate a random digit before entering the loop
random_digit = generate_random_digit()

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
        for recipient_email in recipient_emails:
            # Create the email
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient_email
            message["Subject"] = "Random Digit Generated"

            # Use the same random digit for both recipients
            body = f"Random Digit: {random_digit}"
            message.attach(MIMEText(body, "plain"))

            # Send the email
            server.sendmail(sender_email, recipient_email, message.as_string())
            print(f"Email sent to {recipient_email}")
    print("Emails sent successfully")
except Exception as e:
    print("Error sending emails:", e)

# Check if the random digit sent to both recipients is the same
if random_digit[0] == random_digit[1]:
    print(f"The random digit sent to both recipients is the same: {random_digit}")
else:
    print(f"The random digit sent to both recipients is different: {random_digit}")
