import lib


def crack(coded):
    ciphertext = lib.int_to_ascii(lib.hex_to_int(coded))
    tries = (lib.xor_ascii_repeated(chr(x), ciphertext) for x in xrange(256))
    return max(tries, key=lib.score)

f = open('data/4.txt', 'r')

print max((crack(line.rstrip()) for line in f.readlines()), key=lib.score)
