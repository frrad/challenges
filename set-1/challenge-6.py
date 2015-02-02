import lib


def score(data, n):
    return float(lib.hamming_distance(data[0:n], data[n: 2 * n])) / n


f = open('data/6.txt', 'r')
lines = list(x.rstrip('=\n') for x in f.readlines())


data2 = [lib.int_to_ascii(lib.base_64_to_int(line)) for line in lines]
data = ""
for datum in data2:
    while len(datum) < 45:
        datum = chr(0) + datum
    data += datum


cans = sorted(xrange(2, 40), key=lambda n: score(data, n))
print 'cans', cans

key_length = 29

print "key length", key_length


splits = ["".join([data[x] for x in xrange(start,len(data) ,  key_length)])
          for start in xrange(key_length)]

translated = [lib.crack_brute_force(split, [chr(x) for x in range(
    256)], lib.xor_ascii_repeated, lib.score)[1] for split in splits]

print "".join( [ translated[x % key_length][x / key_length] for x in xrange(len(data)) ])
