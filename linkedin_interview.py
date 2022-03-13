from collections import defaultdict
dictio = defaultdict(list)

def helper(input, level):
    if input.IsInteger():
        dictio[level].append(input)

    else:
        for elem in input.getList():
            if elem.IsInteger():
                dictio[level].append(elem)
            else:
                helper(elem, level + 1)


ans = 0; max_depth = max(dictio.keys())
for level in dictio.keys():
    ans = (max_depth - level + 1) * sum(dictio[level])
