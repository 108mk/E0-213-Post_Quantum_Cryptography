import os;  import binascii;
from signempty import sha3_256  

def keypair():
  secret = sha3_256(os.urandom(32))
  public = sha3_256(secret)
  for i in range(16): public = sha3_256(public)
  return public,secret

def sign(m,secret):
  if type(m) != int: raise Exception('message must be int')
  if m < 0 or m > 15: raise Exception('message must be between 0 and 15')
  sign = secret
  for i in range(m): sign = sha3_256(sign)
  return sign, m 

def open(sm,public):
  if type(sm[1]) != int: raise Exception('message must be int')
  if sm[1] < 0 or sm[1] > 15: raise Exception('message must be between 0 and 15')
  check = sm[0]
  for i in range(16-sm[1]): check = sha3_256(check)
  if sha3_256(check) != public: raise Exception('bad signature')
  return sm[1]
