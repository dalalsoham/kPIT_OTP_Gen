import smtplib
import random
import string

# Function to generate a random 3-digit alphanumeric code
def generate_random_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(3))

# Email configuration
sender_email = "arijeetdas001@gmail.com"
sender_password = "csts whga mkti lyxp"
recipient_emails = ["arijeetdashotmail@gmail.com", "barson0habra@gmail.com"]

# Generate a random code
random_code = generate_random_code()

# Create the email message
message = f"Your random code is: {random_code}"

# Establish an SMTP connection
smtp_server = "smtp.gmail.com"  # Update for your email provider
smtp_port = 587  # Update for your email provider

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

# try:
#     # Log in to the email server
#     server.login(sender_email, sender_password)

#     # Send the first email
#     server.sendmail(sender_email, recipient_emails[0], message)
#     print(f"Email sent to {recipient_emails[0]}")

#     # Send the second email
#     server.sendmail(sender_email, recipient_emails[1], message)
#     print(f"Email sent to {recipient_emails[1]}")

# except smtplib.SMTPException as e:
#     print(f"Email sending failed with error: {e}")

# finally:
#     # Quit the server
#     server.quit()
try:
    # Log in to the email server
    server.login(sender_email, sender_password)

    # Generate a random code
    random_code = generate_random_code()

    # Create the email message
    message = f"Your random code is: {random_code}"

    # Send the first email
    server.sendmail(sender_email, recipient_emails[0], message)
    print(f"Email sent to {recipient_emails[0]}")

    # Send the second email
    server.sendmail(sender_email, recipient_emails[1], message)
    print(f"Email sent to {recipient_emails[1]}")

except smtplib.SMTPException as e:
    print(f"Email sending failed with error: {e}")

finally:
    # Quit the server
    server.quit()
