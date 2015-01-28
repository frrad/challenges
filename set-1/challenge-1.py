decoder = {'1': 1, '0': 0, '3': 3, '2': 2, '5': 5, '4': 4, '7': 7, '6': 6,
           '9': 9, '8': 8, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14,
           'f': 15}

encoder = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H',
           8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
           15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V',
           22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'a', 27: 'b', 28: 'c',
           29: 'd', 30: 'e', 31: 'f', 32: 'g', 33: 'h', 34: 'i', 35: 'j',
           36: 'k', 37: 'l', 38: 'm', 39: 'n', 40: 'o', 41: 'p', 42: 'q',
           43: 'r', 44: 's', 45: 't', 46: 'u', 47: 'v', 48: 'w', 49: 'x',
           50: 'y', 51: 'z', 52: '0', 53: '1', 54: '2', 55: '3', 56: '4',
           57: '5', 58: '6', 59: '7', 60: '8', 61: '9', 62: '+', 63: '/'}


def hex_to_base_64(input_hex):
    if len(input_hex) % 3 != 0:
        print "invalid size"
        return False

    output = ""

    triplets = [input_hex[i:i + 3] for i in range(0, len(input_hex), 3)]
    for triple in triplets:
        value = 0
        for letter in triple:
            value *= 16
            value += decoder[letter]
        output += encoder[value / 64] + encoder[value % 64]

    return output


print hex_to_base_64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
