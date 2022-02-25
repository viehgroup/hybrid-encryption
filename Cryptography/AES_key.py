from Cryptography.RSA_keys import get_public_key, get_private_key
from Cryptography import RSA_keys
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import os
from getpass import getuser
from Crypto.Random import get_random_bytes
import hashlib

# key path for storing the AES key
key_path = f"C:/Users/{getuser()}/Hybrid Encryption/DoNotDelete/AES key.txt"


def str_to_bytes(value: [str, bytes]) -> bytes:
    if isinstance(value, str):
        return value.encode(encoding='utf8')
    return value


def is_AES_key_exist():
    return os.path.isfile(key_path) and os.stat(key_path).st_size != 0


def generate_key():
    return get_random_bytes(128)


def encrypt_key(session_key):
    public_key = get_public_key()
    public_key = RSA.importKey(public_key)
    public_key = PKCS1_OAEP.new(public_key)

    encrypted_aes_key = public_key.encrypt(session_key)

    aes_key_writer = open(key_path, "wb")
    aes_key_writer.write(encrypted_aes_key)
    aes_key_writer.close()


def decrypt_key():

    if not is_AES_key_exist():
        raise FileNotFoundError

    private_key = get_private_key()
    private_key = RSA.importKey(private_key)
    private_key = PKCS1_OAEP.new(private_key)

    aes_key_reader = open(key_path, "rb")
    aes_key = aes_key_reader.read()

    return private_key.decrypt(aes_key)


def get_key():

    if not (is_AES_key_exist() and RSA_keys.is_file_exist()):
        key = generate_key()
        encrypt_key(session_key=key)

    aes_key = decrypt_key()

    return hashlib.sha256(str_to_bytes(aes_key)).digest()




