from cryptography.fernet import Fernet

# Generate a 32-byte base64 key
key = Fernet.generate_key()

# Print the generated key
print(f"Your encryption key: {key.decode()}")