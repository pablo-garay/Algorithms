def print_orderly(a, b):
    if a > b:
        print b, a
    else:
        print a, b

t = int(raw_input().strip())
for a0 in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    dict = {}

    for pos in xrange(len(a)):
        if a[pos] not in dict:
            dict[a[pos]] = []
        dict[a[pos]].append(pos + 1)

    for val in dict:
        if m - val in dict:
            if val != (m - val):
                print_orderly(dict[val][0], dict[m - val][0])
                break

            elif len(dict[val]) >= 2:
                print_orderly(dict[val][0], dict[val][1])
                break
