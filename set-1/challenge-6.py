import lib


def score(data, n):
    return float(lib.hamming_distance(data[0:n], data[n: 2 * n])) / n


f = open('data/6.txt', 'r')
data2 = [lib.base_64_to_ascii(line.rstrip('\n'))
         for line in f.readlines()]

print map(len, data2)

data = ''.join(data2)


cans = sorted(xrange(2, 40), key=lambda n: score(data, n))
print 'cans', cans

key_length = 29

print "key length", key_length


splits = ["".join([data[x] for x in xrange(start, len(data),  key_length)])
          for start in xrange(key_length)]

key = ''.join([lib.crack_brute_force(split, [chr(x) for x in range(
    256)], lib.xor_ascii_repeated, lib.score)[0] for split in splits])

print lib.xor_ascii_repeated(key, data)
