import lib


message = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

ciphered = lib.xor_ascii_repeated('ICE', message)

print '0' + lib.int_to_hex(lib.ascii_to_int(ciphered))
