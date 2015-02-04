import lib


def score(data, n):
    time = 10
    return float(sum((
        lib.hamming_distance(
            data[a * n:(a + 1) * n], data[(a + 1) * n: (a + 2) * n]
        )
        for a in xrange(time)))) / float(n * time)


f = open('data/6.txt', 'r')
data2 = [lib.base_64_to_ascii(line.rstrip('\n'))
         for line in f.readlines()]
data = ''.join(data2)


cans = sorted([(n, score(data, n)) for n in xrange(2, 40)], key=lambda x: x[1])
key_length = cans[0][0]

splits = ["".join([data[x] for x in xrange(start, len(data),  key_length)])
          for start in xrange(key_length)]
key = ''.join([lib.crack_brute_force(split, [chr(x) for x in range(
    256)], lib.xor_ascii_repeated, lib.score)[0] for split in splits])

print 'Key = ', key, '\n'
print lib.xor_ascii_repeated(key, data)
