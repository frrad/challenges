import lib


a = lib.hex_to_int("1c0111001f010100061a024b53535009181c")
b = lib.hex_to_int("686974207468652062756c6c277320657965")

print lib.int_to_hex(a ^ b)
