import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Your email credentials
sender_email = "arijeetdas001@gmail.com"
sender_password = "csts whga mkti lyxp"
recipient_email = "barson0habra@gmail.com"
# SMTP server settings
smtp_server = "smtp.gmail.com"
smtp_port = 587 # Check your email provider's documentation for the correct port

# Create the email
message = MIMEMultipart ()
message["From"] = sender_email
message ["To"] = recipient_email
message["Subject"] = "Sending Email Using Python"
body = "Hello, this is a test email"
message.attach(MIMEText (body,"plain"))

# Connect to the SMTP server and send the email
try:
    server = smtplib. SMTP (smtp_server, smtp_port)
    server.starttls() # Use TLS encryption
    server.login(sender_email, sender_password)
    server.sendmail (sender_email, recipient_email, message.as_string())
    server.quit ()
    print("Email sent successfully")
except Exception as e:
    print("Error sending email:", e)