def array_left_rotation(a, n, k):
    start = k % n
    res = []

    for i in xrange(start, n):
        res.append(a[i])

    for i in xrange(0, start):
        res.append(a[i])

    return res

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str, answer))
