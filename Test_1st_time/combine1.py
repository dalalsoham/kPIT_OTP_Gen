
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
    code = ''.join (random.sample(letters + digits, 6))

    return code

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
            message["To"] = recipient_email  # Set the "To" header only once
            message["Subject"] = "Random Code Generated"
            
            # Generate a random code
            random_code = generate_random_code()
            body = f"Random Code: {random_code}"
            message.attach(MIMEText(body, "plain"))
            
            # Send the email
            server.sendmail(sender_email, recipient_email, message.as_string())
            print(f"Email sent to {recipient_email}")
    print("Emails sent successfully")
except Exception as e:
    print("Error sending emails:", e)

print(f"Random Code: {random_code}")
