import os; import binascii; import hashlib;

def sha3_256(x):
  h = hashlib.sha3_256()
  h.update(x)
  return h.digest()


def keypair():
  secret = sha3_256(os.urandom(32))
  public = sha3_256(secret)
  return public,secret

def sign(message,secret):
  if message != '': raise Exception('nonempty message')
  signedmessage = secret
  return signedmessage

def open(signedmessage,public):
  if sha3_256(signedmessage) != public: raise Exception('bad signature')
  message = ''
  return message
