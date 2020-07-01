from Crypto import Random

r = Random.new()
random = r.read(16)
print (random.hex())
