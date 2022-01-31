from collections import Counter
a = [1, 1, 3, 4]
b = [1, 2, 3, 4]
res_perm = []
res_perm2 = []
res_comb = []

def permutations_unique(partial, rest, k):
    if len(partial) == k:
        res_perm.append(partial)
        return

    for item in rest.keys():
        rest[item] -= 1
        if rest[item] == 0:
            del rest[item]
        permutations_unique(partial + [item], rest, k)
        rest[item] += 1

def permutations(partial, rest, k):
    if len(partial) == k:
        res_perm2.append(partial)
        return

    for item in list(rest):
        rest.remove(item)
        permutations(partial + [item], rest, k)
        rest.add(item)

def combinations(partial, iterable, last, k):
    if len(partial) == k:
        res_comb.append(partial)
        return

    for i in xrange(last, len(iterable)):
        combinations(partial + [iterable[i]], iterable, i + 1, k)


permutations_unique([], Counter(a), len(a)); print res_perm
permutations([], set(a), 3); print res_perm2
combinations([], b, 0, len(b) - 1); print res_comb
