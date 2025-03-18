import hashlib

import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def hash_password(password):
	hash_type = 'sha256'
	hash_func = getattr(hashlib, hash_type) # get hashlib.sha256 form hashlib module
	hash_obj = hash_func() # create hash object by calling the function
	# hash_obj = hashlib.sha256() same as above 3 lines

	hash_obj.update(password.encode())
	#print(hash_obj.digest())

	hashed_password = hash_obj.hexdigest()
	return hashed_password

#print (hash_password('hello'))

def generate_key_from_password(password:str, salt:bytes) -> bytes:
	
	kdf = PBKDF2HMAC (
		algorithm = hashes.SHA256(),
		length = 32,
		salt = salt,
		iterations = 100000,
		backend = default_backend()
	)
	return kdf.derive(password.encode()) #generate 32 byte key
	

def encrypt_note(plaintext: str, key: bytes) -> tuple:
	#Encrypts a plaintext string using AES-GCM
	iv = os.urandom(12)
	cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend = default_backend())
	encryptor = cipher.encryptor()
	
	ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
	
	return iv, ciphertext, encryptor.tag
	
def decrypt_note(iv: bytes, ciphertext: bytes, tag: bytes, key: bytes) -> str:
	#Decrypts an AES-GCM encrypted text
	cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend = default_backend())
	
	decryptor = cipher.decryptor()
	
	return (decryptor.update(ciphertext) + decryptor.finalize()).decode()
