import lib

coded = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

a = lib.hex_to_int(coded)
print a


for key_char in [chr(n) for n in range(256)]:
    key = key_char * (len(coded) /2)
    print lib.int_to_ascii(lib.ascii_to_int(key) ^ a)

