#
# def permutations(n):
#
#     for i in xrange(n):
#         for j in


def permutations_set(set_items):
    permutations_list = []
    # set_items = set(li)

    if len(set_items) == 1:  # base case
        for item in set_items:
            return [[item]]

    for item in set_items:
        set_items.remove(item)

        for permutation in permutations_set(set_items):
            permutations_list += [[item] + permutation]
            # permutations_list.append([item] + permutation) #
            # this does the same as previous line

        set_items.add(item)

    return permutations_list


def permutations(li):
    return permutations_set(set(li))

result = permutations(range(4))
print len(result)
print result
