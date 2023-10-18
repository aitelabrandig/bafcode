import os
import hashlib
from cryptography.fernet import Fernet
from dotenv import load_dotenv
load_dotenv()
# Key management
SECRET_KEY = os.environ.get("FRAMEWORK_SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("Secret key not set in environment variables!")

cipher_suite = Fernet(SECRET_KEY)


def generate_key():
    """
    Generate a new Fernet key. It's essential to keep this key safe.
    """
    return Fernet.generate_key()


def encrypt_data(data: str) -> bytes:
    """
    Encrypt a piece of data.

    Args:
    - data (str): Data to be encrypted.

    Returns:
    - bytes: Encrypted data.
    """
    if not isinstance(data, bytes):
        data = data.encode('utf-8')
    encrypted_data = cipher_suite.encrypt(data)
    return encrypted_data


def decrypt_data(encrypted_data: bytes) -> str:
    """
    Decrypt a piece of encrypted data.

    Args:
    - encrypted_data (bytes): Encrypted data.

    Returns:
    - str: Decrypted data.
    """
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data.decode('utf-8')


def hash_data(data: str, salt: str = None) -> str:
    """
    Generate a hash of the data using SHA-256. Can be used for password hashing.

    Args:
    - data (str): Data to be hashed.
    - salt (str): Optional salt to add extra security to the hash.

    Returns:
    - str: Hashed data.
    """
    if salt:
        data += salt
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


# # Example usage:
# if __name__ == "__main__":
#     # Encryption and decryption
#     encrypted = encrypt_data("Hello, World!")
#     print(f"Encrypted: {encrypted}")
#     decrypted = decrypt_data(encrypted)
#     print(f"Decrypted: {decrypted}")

#     # Hashing
#     hashed = hash_data("password", salt="somesalt")
#     print(f"Hashed: {hashed}")
