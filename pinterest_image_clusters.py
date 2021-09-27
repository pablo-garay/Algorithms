# A -> [B, I, K]
# B -> [A, D]
# C -> [E]
# D -> []
# E -> []
# F -> []
# G -> [K]
# I -> []
# K -> []

# (A, B, D, I, G, K), (C, E), and (F)

from collections import defaultdict

# Efficient implementation of union-find would be using path splitting/path halving
# Makes find operation O(log n)
def union(i1, i2, parent):
    parent1, parent2 = (find(i1, parent), find(i2, parent))
    if parent1 == parent2:
        return

    # parent1, parent2 = parent1, parent2 if parent1 <= parent2 else parent2
    parent[i1] = parent[i2] = min(parent1, parent2)


def find(i, parent):
    if i == parent[i]:
        return i
    else:
        return find(parent[i], parent)


# Traversing n elems, each time taking O(log n) makes complexity O(n log n)
def solve(dictio):
    parent = {key: key for key in dictio.keys()}
    print parent

    for key in dictio.keys():
        for value in dictio[key]:
            union(key, value, parent)

    res = defaultdict(set)

    for key in parent:
        for val in parent[key]:
            res[val].add(key)

    for key in res:
        print res[key]


solve({
    "A": ["B", "I", "K"],
    "B": ["A", "D"],
    "C": ["E"],
    "D": [],
    "E": [],
    "F": [],
    "G": ["K"],
    "I": [],
    "K": []
})
