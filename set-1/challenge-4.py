import lib


def decrypt(ciphertext, key):
    key_repeated = key * (len(ciphertext) / 2)
    return lib.int_to_ascii(
        lib.ascii_to_int(key_repeated) ^ lib.hex_to_int(ciphertext)
    )


def score(cleartext):
    answer = 0
    for letter in cleartext:
        code = ord(letter)
        if 64 < code < 91 or code == 32 or 96 < code < 123:
            answer += 1
    return answer


def crack(coded):
    tries = [decrypt(coded, chr(x)) for x in xrange(256)]
    return max(tries, key=score)

f = open('data/4.txt', 'r')

print max([crack(line.rstrip()) for line in f.readlines()], key=score)
