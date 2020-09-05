import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from zxcvbn import zxcvbn
from math import log


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
        decoded_str = dec.decrypt(str_to_decrypt)
        output.append(decoded_str.decode())
    return output


def get_strength(password):
    result = zxcvbn(password)

    green = 25 * log(result.get('guesses'), 16)
    if green > 255:
        green = 255
    red = 255 - green

    if green <= 50:
        strength = 'Weak'
    elif 50 < green <= 100:
        strength = 'Medium'
    elif 100 < green < 200:
        strength = 'Strong'
    else:
        strength = 'Very Strong'

    return red, green, strength


def check_inputs(url, login, password):
    if not url:
        return "URL field can't be blank"
    elif not login:
        return "Login field can't be blank"
    elif not password:
        return "Password field can't be blank"
    else:
        return False
