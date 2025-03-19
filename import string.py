import string
import random

chars = " "+string.punctuation + string.digits +string.ascii_letters
chars = list(chars)
key =chars.copy()
random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")

#encrypt



plain_text =input("enter a message to encrypt: ")
ciphertext =""

for letter in plain_text:
    index = chars.index(letter)
    ciphertext += key[index]

print(f"original message: {plain_text}")
print(f"encrypt message: {ciphertext}")

#decrypt
ciphertext =input("enter a message to decrypt: ")
plain_text =""

for letter in ciphertext:
    index = key.index(letter)
    plain_text += chars[index]

print(f"original message: {ciphertext}")
print(f"encrypt message: {plain_text}")