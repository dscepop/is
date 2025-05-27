#pip install pycryptodome

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(pad(plaintext.encode(), 8))

def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    return unpad(cipher.decrypt(ciphertext), 8).decode()

# Ensure 8-byte key (strict)
key = input("Enter 8-byte key (e.g., 'mykey123'): ").encode()
assert len(key) == 8, "Key must be exactly 8 bytes!"

text = input("Enter text: ")
mode = input("Encrypt (e) or decrypt (d): ").lower()[0]

if mode == 'e':
    encrypted = des_encrypt(key, text)
    print("Encrypted (hex):", encrypted.hex())
else:
    ciphertext = bytes.fromhex(input("Enter ciphertext (hex): "))
    print("Decrypted:", des_decrypt(key, ciphertext))


#output

Enter 8-byte key (e.g., 'mykey123'): mydeskey
Enter text: Secure123
Encrypt (e) or decrypt (d): e
Encrypted (hex): 787c93d9dc6be0f92ab6a636324f363c
