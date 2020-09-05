import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


def generate_key(username):
    key = username.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=username[::-1].encode(),
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(key))
    return key


def encrypt_data(key, inputs):
    output = []
    for str_to_encrypt in inputs:
        str_to_encrypt = str_to_encrypt.encode()

        enc = Fernet(key)
        output.append(enc.encrypt(str_to_encrypt))
    return output


def decrypt_data(key, inputs):
    output = []
    for str_to_decrypt in inputs:
        dec = Fernet(key)
        output.append(dec.decrypt(str_to_decrypt))
    return output
