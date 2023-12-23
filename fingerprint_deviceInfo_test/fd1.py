from cryptography.fernet import Fernet
import hashlib
import random
import string
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client
import platform
import subprocess
import wmi

def get_serial_number():
    system = platform.system()
    if system == 'Windows':
        try:
            c = wmi.WMI()
            for item in c.Win32_BIOS():
                return item.SerialNumber
        except Exception as e:
            print("Error occurred while fetching serial number using WMI:", e)
            try:
                output = subprocess.check_output(['wmic', 'bios', 'get', 'serialnumber']).decode().split('\n')
                return output[1].strip()
            except Exception as e:
                print("Error occurred while fetching serial number using WMIC command:", e)
                return "Serial Number not found"
    elif system == 'Linux':
        try:
            with open('/sys/class/dmi/id/product_serial') as f:
                return f.read().strip()
        except FileNotFoundError:
            try:
                output = subprocess.check_output(['dmidecode', '-s', 'system-serial-number']).decode().strip()
                return output
            except Exception as e:
                print("Error occurred while fetching serial number on Linux:", e)
                return "Serial Number not found"
    elif system == 'Darwin':  # For MacOS
        try:
            output = subprocess.check_output(["system_profiler", "SPHardwareDataType"])
            output = output.decode("utf-8")
            serial_number = list(filter(lambda x: "Serial Number" in x, output.split("\n")))[0].split(":")[1].strip()
            return serial_number
        except Exception as e:
            print("Error occurred while fetching serial number on MacOS:", e)
            return "Serial Number not found"
    else:
        return "Platform not supported"

# Generate a random encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to generate a random 6-digit code
def generate_random_code():
    return ''.join(random.choices(string.digits, k=6))

# Function to encrypt and hash the message
def encrypt_and_hash(message):
    encrypted_message = cipher_suite.encrypt(message.encode())
    full_hash = hashlib.sha256(encrypted_message).hexdigest()
    last_six_digits = full_hash[-6:]
    return full_hash, last_six_digits

# Function to send the first 3 digits to the email
def send_email_first_part(first_part, receiver_email):
    sender_email = 'arijeetdas001@gmail.com'
    password = 'csts whga mkti lyxp'

    message = MIMEText(f"First 3 digits of OTP: {first_part}")
    message['Subject'] = 'First 3 Digits of OTP'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# Function to send the last 3 digits to the phone using Twilio
def send_otp_sms(last_part, recipient_phone_number):
    twilio_account_sid = "AC14bf1e53e20c5a64cd0dc790c14ec94b"  # Enter your Twilio account SID
    twilio_auth_token = "267ce793e1ade29fc5c90392913b3cef"  # Enter your Twilio auth token
    twilio_phone_number = "+12055649437"  # Enter your Twilio phone number

    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        to=recipient_phone_number,
        from_=twilio_phone_number,
        body=f"Your last 3 digits of OTP is: {last_part}"
    )
    print(f"OTP sent to {recipient_phone_number}")

# Main program
if __name__ == "__main__":
    plain_text = input("Enter the plain text message: ")

    # Encrypt the message and extract the last 6 digits of the hash
    full_hash, last_six_digits = encrypt_and_hash(plain_text)

    # Get the first 3 and last 3 digits
    first_part = last_six_digits[:3]
    last_part = last_six_digits[3:]

    # Get the device's serial number
    device_serial_number = get_serial_number()

    print(f"Device Serial Number: {device_serial_number}")

    # Simulate sending the first 3 digits via email and last 3 digits via phone using Twilio
    receiver_email = input("Enter your email address: ")
    recipient_phone_number = input("Enter your phone number: ")

    send_email_first_part(first_part, receiver_email)
    send_otp_sms(last_part, recipient_phone_number)
    print("OTP sent via email and phone.")

    # User enters the received 6-digit code
    entered_code = input("Enter the 6-digit code received via email and phone: ")

    # Verify if entered code matches the last 6 digits of the hash
    if entered_code == last_six_digits:
        print("Code matched!")
    else:
        print("Code not matched!")

    # Display the full hash code generated
    print(f"The full hash code is: {full_hash}")
