from cryptography.fernet import Fernet

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

# Prompt user for input
plaintext_message = input("Enter the message you want to encrypt: ")

# Generate a random key (you can replace this with your own key)
key = generate_key()

# Encrypt the message
ciphertext = encrypt_message(key, plaintext_message)

print(f"Plaintext: {plaintext_message}")
print(f"Encrypted message: {ciphertext}")

# Decrypt the message
decrypted_message = decrypt_message(key, ciphertext)

print(f"Decrypted message: {decrypted_message}")
