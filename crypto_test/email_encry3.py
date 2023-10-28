from cryptography.fernet import Fernet
import smtplib
import imaplib
import email
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

def receive_confirmation(to_email):
    from_email = 'manasahinath8250@gmail.com'  # Replace with your email address
    password = 'ovvo qsar fwkf aher'  # Replace with your email password

    # Connect to the IMAP server and fetch the latest email
    with imaplib.IMAP4_SSL('imap.gmail.com') as server:  # Replace with your IMAP server
        server.login(from_email, password)
        server.select('inbox')

        status, email_data = server.search(None, 'ALL')
        email_ids = email_data[0].split()

        if email_ids:
            latest_email_id = email_ids[-1]
            status, msg_data = server.fetch(latest_email_id, '(RFC822)')
            raw_email = msg_data[0][1]

            # Parse the email content
            msg = email.message_from_bytes(raw_email)
            subject = msg['subject']
            body = None

            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True)
                    break

            return body.decode('utf-8').strip()

    return None

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

# Receive confirmation and verify the message
confirmation = receive_confirmation(to_email)

if confirmation == str(ciphertext):
    print("Message successfully verified.")
    decrypted_message = decrypt_message(key, ciphertext)
    print(f"Decrypted message: {decrypted_message}")
else:
    print("Message verification failed. The received message does not match the sent message.")
