import hmac
import hashlib

# Secret key used for HOTP
secret_key = b'SecretKey123'  # Replace with your secret key

# Function to generate HOTP
def generate_hotp(secret, counter, length=6):
    hmac_digest = hmac.new(secret, counter.to_bytes(8, byteorder='big'), hashlib.sha1).digest()
    offset = hmac_digest[-1] & 0x0F
    binary_code = ((hmac_digest[offset] & 0x7F) << 24 |
                   (hmac_digest[offset + 1] & 0xFF) << 16 |
                   (hmac_digest[offset + 2] & 0xFF) << 8 |
                   (hmac_digest[offset + 3] & 0xFF))
    hotp = str(binary_code % 10 ** length)
    return hotp.zfill(length)

# Generate a counter (you can use a time-based counter in practice)
counter = 1

# Generate HOTP
hotp_code = generate_hotp(secret_key, counter)

# Send the HOTP code
# Add your code to send the HOTP as per your requirements (email, SMS, etc.)

# Prompt the user for input
user_input = input("Enter the 6-digit OTP: ")

# Check if the input matches the generated HOTP code
if user_input == hotp_code:
    print("Code matched")
else:
    print("Code mismatch has occurred")

# Print the original HOTP code
print(f"Original HOTP Code: {hotp_code}")
