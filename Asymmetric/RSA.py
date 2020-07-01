from Crypto.PublicKey import RSA
from hashlib import sha512

keyPair = RSA.generate(bits=1024)
print(f"Public key: (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
print(f"Private key: (n={hex(keyPair.n)}, e={hex(keyPair.d)})")

#sign
msg = b'Golden Chip Company'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
signature = pow(hash, keyPair.d, keyPair.n)
print(hash)
print("conan")
print("Signature: ", hex(signature))

msg = b'Golden Chip Company'
# RSA verify signature
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature valid:", hash == hashFromSignature)