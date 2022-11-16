import random

def genKey():
  return [[hex(random.randrange(0, 255)) for c in range(4)] for i in range(4)]

print(genKey())