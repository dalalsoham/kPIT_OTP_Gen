# not valid code that i want


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
    return encrypted_message

# Function to send an email
def send_email(encrypted_message, plain_text):
    sender_email = 'sdjack2826@gmail.com'
    receiver_email = 'barson0habra@gmail.com'
    password = 'auxg xfnh recc ohzz'

    message = MIMEText(f"Encrypted Message: {encrypted_message}\nPlain Text: {plain_text}")
    message['Subject'] = 'Encrypted Message'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# Main program
if __name__ == "__main__":
    plain_text = input("Enter the plain text message: ")

    # Hash the message
    hashed_message = hashlib.sha256(plain_text.encode()).hexdigest()

    # Encrypt the message
    encrypted_message = encrypt_and_hash(plain_text)

    # Send the email
    send_email(encrypted_message, plain_text)

    print("Message sent successfully!")

    # Simulate receiving the email and extracting the encrypted message
    received_encrypted_message = input("Enter the received encrypted message: ")
    received_plain_text = input("Enter the received plain text: ")

    # Verify if the received message matches the hash
    if hashlib.sha256(received_plain_text.encode()).hexdigest() == hashed_message and cipher_suite.decrypt(received_encrypted_message).decode() == received_plain_text:
        print("Message verified!")
    else:
        print("Message not verified!")
