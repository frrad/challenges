import lib


def hex_to_base_64(input_hex):
    return lib.int_to_base_64(lib.hex_to_int(input_hex))


print hex_to_base_64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
