import signbit
from signempty import sha3_256

def keypair():
  keys = [signbit.keypair() for n in range(256)]
  public,secret = zip(*keys)
  return  public,secret

def sign(message,secret):
  msg = message.to_bytes(200, byteorder="little")
  h = sha3_256(msg)
  hbits = [1 & (h[i//8])>>(i%8) for i in range(256)]
  sigs = [signbit.sign(hbits[i],secret[i]) for i in range(256)]
  return sigs, message

def open(sm,public):
  message = sm[1]
  msg = message.to_bytes(200, byteorder="little")
  h = sha3_256(msg)
  hbits = [1 & (h[i//8])>>(i%8) for i in range(256)]
  for i in range(256):
    if hbits[i] != signbit.open(sm[0][i],public[i]):
      raise Exception('bit %d of hash does not match' % i)
  return message

# example:
# >>> import lamport
# >>> pk,sk = lamport.keypair()
# >>> sm = lamport.sign('hello',sk)
# >>> lamport.open(sm,pk)
# 'hello'
