from cryptography.fernet import Fernet
from cryptography.hazmat import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import hashlib
import random
import string
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client

# Generate an RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# Generate a random encryption key for symmetric encryption
symmetric_key = Fernet.generate_key()
cipher_suite = Fernet(symmetric_key)

# Function to generate a random 6-digit code
def generate_random_code():
    return ''.join(random.choices(string.digits, k=6))

# Function to encrypt and hash the message
def encrypt_and_hash(message):
    encrypted_message = cipher_suite.encrypt(message.encode())
    full_hash = hashlib.sha256(encrypted_message).hexdigest()
    last_six_digits = full_hash[-6:]
    return encrypted_message, full_hash, last_six_digits

# Function to generate a digital signature
def generate_signature(message):
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

# Function to verify a digital signature
def verify_signature(message, signature, public_key):
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print(f"Signature verification failed: {e}")
        return False

# Function to send the first 3 digits, signature, and public key to the email
def send_email_first_part(first_part, signature, receiver_email):
    sender_email = 'arijeetdas001@gmail.com'
    password = 'csts whga mkti lyxp'

    message = MIMEText(f"First 3 digits of OTP: {first_part}")
    message['Subject'] = 'First 3 Digits of OTP'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.sendmail(sender_email, receiver_email, public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

# Main program
if __name__ == "__main__":
    plain_text = input("Enter the plain text message: ")

    # Encrypt the message and extract the last 6 digits of the hash
    encrypted_message, full_hash, last_six_digits = encrypt_and_hash(plain_text)

    # Get the first 3 and last 3 digits
    first_part = last_six_digits[:3]
    last_part = last_six_digits[3:]

    # Generate a digital signature
    signature = generate_signature(plain_text.encode())

    # Simulate sending the first 3 digits, signature, and public key via email
    receiver_email = input("Enter your email address: ")

    send_email_first_part(first_part, signature, receiver_email)
    print("First part of OTP, signature, and public key sent via email.")

    # User enters the received 6-digit code
    entered_code = input("Enter the 6-digit code received via email: ")

    # Verify if entered code matches the last 6 digits of the hash
    if entered_code == last_six_digits:
        print("Code matched!")
    else:
        print("Code not matched!")

    # Verify the digital signature
    if verify_signature(plain_text.encode(), signature, public_key):
        print("Signature verified.")
    else:
        print("Signature verification failed.")

    # Display the full hash code generated
    print(f"The full hash code is: {full_hash}")
