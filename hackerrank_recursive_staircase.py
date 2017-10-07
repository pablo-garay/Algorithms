num_ways = [0, 1, 2, 4]

for n in range(20):
    last = len(num_ways) - 1

    if n > last:
        for i in xrange(last + 1, n + 1):
            num_ways.append(num_ways[i - 1] + num_ways[i - 2] + num_ways[i - 3])

    print num_ways[n]



