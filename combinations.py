def combinations(so_far, curr, iterable, k):
    if len(so_far) == k:
        res.append(so_far)
        return

    for i in xrange(curr, len(iterable)):
        combinations(so_far + [iterable[i]], i + 1, iterable, k)


# li = [1, 2, 3, 4]
li = [1, 2, 3, 4, 5]
res = []; combinations([], 0, li, 2); print res
res = []; combinations([], 0, li, 3); print res
res = []; combinations([], 0, li, 1); print res
res = []; combinations([], 0, li, 4); print res