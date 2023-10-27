from cryptography.fernet import Fernet
import smtplib
from email.mime.text import MIMEText

def generate_key():
    return Fernet.generate_key()

def encrypt_message(key, message):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(key, encrypted_message):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

def send_email(to_email, subject, message):
    from_email = 'sdjack2826@gmail.com'  # Replace with your email address
    password = 'auxg xfnh recc ohzz'  # Replace with your email password

    # Create the email content
    msg = MIMEText(message.decode())  # Convert bytes to string
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Connect to the SMTP server and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Replace with your SMTP server and port
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, [to_email], msg.as_string())

# Prompt user for input
plaintext_message = input("Enter the message you want to encrypt: ")
to_email = input("Enter the recipient's email address: ")

# Generate a random key (you can replace this with your own key)
key = generate_key()

# Encrypt the message
ciphertext = encrypt_message(key, plaintext_message)

print(f"Plaintext: {plaintext_message}")
print(f"Encrypted message: {ciphertext}")

# Send the encrypted message via email
subject = "Encrypted Message"
send_email(to_email, subject, ciphertext)

# Decrypt the message
decrypted_message = decrypt_message(key, ciphertext)

print(f"Decrypted message: {decrypted_message}")
