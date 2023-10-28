from cryptography.fernet import Fernet
import hashlib
import smtplib
from email.mime.text import MIMEText

# Generate a random encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to encrypt and hash the message
def encrypt_and_hash(message):
    encrypted_message = cipher_suite.encrypt(message.encode())
    hashed_message = hashlib.sha256(encrypted_message).hexdigest()
    return encrypted_message, hashed_message

# Function to send an email
def send_email(encrypted_message, hashed_message):
    sender_email = 'sdjack2826@gmail.com'
    receiver_email = 'barson0habra@gmail.com'
    password = 'auxg xfnh recc ohzz'

    message = MIMEText(f"Encrypted Message: {encrypted_message}\nHashed Message: {hashed_message}")
    message['Subject'] = 'Encrypted Message'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# Main program
if __name__ == "__main__":
    plain_text = input("Enter the plain text message: ")

    # Encrypt and hash the message
    encrypted_message, hashed_message = encrypt_and_hash(plain_text)

    # Send the email
    send_email(encrypted_message, hashed_message)

    print("Message sent successfully!")

    # Simulate receiving the email and extracting the encrypted and hashed messages
    received_encrypted_message = input("Enter the received encrypted message: ")
    received_hashed_message = input("Enter the received hashed message: ")

    # Verify if the received message matches the hashed message
    if hashlib.sha256(received_encrypted_message.encode()).hexdigest() == received_hashed_message:
        print("Message verified!")
    else:
        print("Message not verified!")
