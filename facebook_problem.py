def partial_reversing(li, first, second):
    left, right = first, second

    while left < right:
        li[first], li[second] = li[second], li[first]
        left += 1
        right -= 1

    return li

print partial_reversing(["a", "b", "c", "d", "e", "f"], 2, 4) # a b e d c f
