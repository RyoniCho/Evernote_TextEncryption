import base64
import hmac
import hashlib

from pdkpf2_modi import PBKDF2
from Crypto.Cipher import AES

password=input("password?")
encryptedText=input("text?")


keylength = 128
iterations = 50000
matches = 0



bintxt = base64.b64decode(encryptedText)
salt = bintxt[4:20]
salthmac = bintxt[20:36]
iv = bintxt[36:52]
ciphertext = bintxt[52:-32]
body = bintxt[0:-32]
bodyhmac = bintxt[-32:]

## use the password to generate a digest for the encrypted body
## if it matches the existing digest we can assume the password is correct
keyhmac = PBKDF2(password, salthmac, iterations, hashlib.sha256).read(keylength/8)
testhmac = hmac.new(keyhmac, body, hashlib.sha256)
match_hmac = hmac.compare_digest(testhmac.digest(),bodyhmac)

if match_hmac:
    key = PBKDF2(password, salt, iterations, hashlib.sha256).read(keylength/8)
    aes = AES.new(key, AES.MODE_CBC, iv)
    plaintext = aes.decrypt(ciphertext)
    
    print(plaintext.decode('utf-8'))
    matches += 1
    print ('Decrypted {} encryptions'.format(matches))

 