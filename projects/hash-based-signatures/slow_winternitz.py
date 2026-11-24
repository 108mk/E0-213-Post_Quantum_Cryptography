import weak_winternitz

def keypair():
  keys = [weak_winternitz.keypair() for n in range(2)]
  public,secret = zip(*keys)
  return public,secret

def sign(m,secret):
  sign0 = weak_winternitz.sign(m,secret[0])
  sign1 = weak_winternitz.sign(16-m,secret[1])
  return sign0, sign1, m 

def open(sm,public):
  m0 = weak_winternitz.open(sm[0],public[0])
  m1 = weak_winternitz.open(sm[1],public[1])
  if m0 != sm[2] or  m1 != (16-sm[2]): raise Exception('Invalid signature')
  return sm[2]
