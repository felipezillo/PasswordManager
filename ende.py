# from Crypto.Cipher import DES
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os


class Ende:
    def __init__(self, key):
        # self._key = str(os.getenv('KEY'))
        # self.obj = DES.new(self._key, DES.MODE_ECB)
        load_dotenv()
        self._key = os.getenv('FERNET_KEY').encode()
        self.obj = Fernet(self._key)

    def encrypt(self, plainText: str) -> str: 
        return self.obj.encrypt(plainText.encode())
    
    def decrypt(self, cipheredText: str) -> str:
        return self.obj.decrypt(cipheredText).decode()
    