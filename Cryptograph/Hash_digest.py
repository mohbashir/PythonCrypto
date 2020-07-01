from Crypto.Hash import SHA256


def hashMessage(msg):
    # convert string to byte array
    msg = bytes(msg, 'utf-8')

    # init hashing to SHA256
    h = SHA256.new()

    # do hashing and hex digest
    h.update(msg)
    return h.hexdigest()


print(hashMessage("hello"))
