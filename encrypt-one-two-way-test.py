#!/usr/bin/env python3

from Crypto.Cipher import AES
import uuid
import hashlib
import binascii
import os

# A function to hash password using sha256 salt

def hash_it_with_salt(strg):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + strg.encode()).hexdigest() + ':' + salt

#Data Entry
print ()
print ("----------------------------------------------------")
print (" Encryption Test")
print ("----------------------------------------------------")
print (" 1: One way")
print (" 2: Two way")
print ("----------------------------------------------------")
strgOrig = input("|-> Enter String :")
print ()
print (" 1: One way (using sha256 + salt)")
print ("----------------------------------------------------")
print ("|-> hashed = "+hash_it_with_salt(strgOrig));

print ()
print (" 1: Two way (AES)")
print ("----------------------------------------------------")

pskey =  binascii.hexlify(os.urandom(16))
print("|-> Generated Key: "+pskey.decode('utf-8'))
  
# ENCRYPT: AES
  
obj = AES.new(pskey, AES.MODE_CBC, 'This is an IV456')
storeLen = len(strgOrig)
if storeLen < 16:
	diflen = (32-storeLen)
	strgOrig = strgOrig+pskey.decode('utf-8')[0:diflen]
	
ciphertext = obj.encrypt(strgOrig)
print ()
print ("|->  ENCRYPT: AES > "+str(ciphertext))
  
# DECRYPT: AES
  
obj2 = AES.new(pskey, AES.MODE_CBC, 'This is an IV456')

if storeLen < 16:
	plaintext = obj2.decrypt(ciphertext)[0:storeLen]
else:
	plaintext = obj2.decrypt(ciphertext)
	
print ()
os.system('color 7')
print ("|->  DECRYPT: AES > "+str(plaintext))
print ("----------------------------------------------------")