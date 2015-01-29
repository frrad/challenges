import lib


def decrypt(ciphertext, key):
    key_repeated = key * (len(ciphertext) / 2)
    return lib.int_to_ascii(
        lib.ascii_to_int(key_repeated) ^ lib.hex_to_int(ciphertext)
    )


def crack(coded):
    tries = [decrypt(coded, chr(x)) for x in xrange(256)]
    return max(tries, key=lib.score)

f = open('data/4.txt', 'r')

print max([crack(line.rstrip()) for line in f.readlines()], key=lib.score)
