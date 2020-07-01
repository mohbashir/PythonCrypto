from Crypto import Random

def generateRan(size):
    rand = Random.new()
    random = rand.read(size)

    return random.hex()

print(generateRan(16))