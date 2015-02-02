import lib


code = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
ascii_code = lib.int_to_ascii(lib.hex_to_int(code))

answer = lib.crack_brute_force(
    ascii_code, [chr(x) for x in range(256)], lib.xor_ascii_repeated, lib.score)
print answer[1]
