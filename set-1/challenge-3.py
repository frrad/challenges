import lib


coded = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"


def decrypt(ciphertext, key):
    key_repeated = key * (len(ciphertext) / 2)
    return lib.int_to_ascii(
        lib.ascii_to_int(key_repeated) ^ lib.hex_to_int(coded)
    )


def score(cleartext):
    answer = 0
    for letter in cleartext:
        code = ord(letter)
        if 64 < code < 91 or code == 32 or 96 < code < 123:
            answer += 1
    return answer


tries = [(chr(x), decrypt(coded, chr(x))) for x in xrange(256)]
print max(tries, key=lambda x: score(x[1]))
