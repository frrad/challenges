decoder = {'1': 1, '0': 0, '3': 3, '2': 2, '5': 5, '4': 4, '7': 7, '6': 6,
           '9': 9, '8': 8, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14,
           'f': 15}

encoder = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
           8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e',
           15: 'f'}


# Translate a hex encoded string into integer
def hex_to_int(hex_input):
    output = 0
    for letter in hex_input:
        output *= 16
        output += decoder[letter]
    return output

# Translate into to hex encoded string
def int_to_hex(int_input):
    output = ""
    while int_input > 0:
        output = encoder[int_input % 16] + output
        int_input /= 16
    return output
