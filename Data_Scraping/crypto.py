#!/usr/bin/python

import Crypto.Random
from Crypto.Cipher import AES
import hashlib
import base64

# Initialization Vector For Randomizing Pattern For Makng It Hard For Rainbow Table Attack 
# We Hashed Initial Vector With MD5 Hash Algorithm For Acquiring 16 byte Size of IV 

#Salt Size
SALT_SIZE = 16

# number of iterations in the key generation
NUMBER_OF_ITERATIONS = 20

# the size multiple required for AES
AES_MULTIPLE = 16

def generate_key(password, salt, iterations):
    assert iterations > 0
    key = password + salt
    for i in range(iterations):
        key = hashlib.sha256(key).digest()  
    return key

def pad_text(text, multiple):
    extra_bytes = len(text) % multiple
    padding_size = multiple - extra_bytes
    padding = chr(padding_size) * padding_size
    padded_text = text + padding
    return padded_text

def unpad_text(padded_text):
    padding_size = ord(padded_text[-1])
    text = padded_text[:-padding_size]
    return text

def encrypt(plaintext, password, IV):
    IV = hashlib.md5(IV).digest()
    salt = Crypto.Random.get_random_bytes(SALT_SIZE)
    key = generate_key(password, salt, NUMBER_OF_ITERATIONS)
    cipher = AES.new(key, AES.MODE_CBC, IV)
    padded_plaintext = pad_text(plaintext, AES_MULTIPLE)
    ciphertext = cipher.encrypt(padded_plaintext)
    ciphertext_with_salt = salt + ciphertext
    return base64.urlsafe_b64encode(ciphertext_with_salt)

def decrypt(ciphertext, password, IV):
    ciphertext = base64.urlsafe_b64decode(ciphertext)
    IV = hashlib.md5(IV).digest()
    salt = ciphertext[0:SALT_SIZE]
    ciphertext_sans_salt = ciphertext[SALT_SIZE:]
    key = generate_key(password, salt, NUMBER_OF_ITERATIONS)
    cipher = AES.new(key, AES.MODE_CBC, IV)
    padded_plaintext = cipher.decrypt(ciphertext_sans_salt)
    plaintext = unpad_text(padded_plaintext)
    return plaintext

def gen_hash_file(fname):
    file = open(fname)
    hash = hashlib.sha512()
    buffer_size = 4096
    while(file.read(buffer_size)):
        hash.update(file.read(buffer_size))
    return hash.hexdigest()
