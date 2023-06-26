import base64
import hmac
import hashlib
import os
import binascii


from pdkpf2_modi import PBKDF2
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]

keylength = 128
iterations = 50000
matches = 0


password=input("password?")
targetText=input("text?")

payload = bytes()
payload += b'ENC0'

# Three  random values
salt = os.urandom(16)
salthmac = os.urandom(16)
iv = os.urandom(16)

payload += salt
payload += salthmac
payload += iv # we'll append the ciphertext last

print (f'salt: {binascii.hexlify(salt)}')
print (f'salthmac: {binascii.hexlify(salthmac)}')
print (f'iv: {binascii.hexlify(iv)}')

key = PBKDF2(password, salt, iterations, hashlib.sha256).read(keylength/8)

aes = AES.new(key, AES.MODE_CBC, iv)

targetText= pad(targetText)
print(targetText)

encodedText = aes.encrypt(bytes(targetText,'utf-8'))

print(encodedText)

payload+=encodedText






# Derive key for HMAC validation
keyhmac = PBKDF2(password, salthmac, iterations,hashlib.sha256).read(keylength/8)

hd = hmac.new(keyhmac, None, hashlib.sha256)
hd.update(payload)
digest = hd.digest()

payload += digest


finalResult=base64.b64encode(payload)

print(finalResult)