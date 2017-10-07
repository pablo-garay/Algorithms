
sorted_array = sorted([54,26,93,17,77,31,44,55,20])
print sorted_array

array_size = len(sorted_array)
start = 0
end = array_size - 1


def binary_search(num_searched, array, start, end):
    if start > end:
        return False

    middle = (start + end) / 2

    if num_searched == array[middle]:
        return True
    elif num_searched > array[middle]:
        return binary_search(num_searched, array, middle + 1, end)
    else:
        return binary_search(num_searched, array, start, middle - 1)


# A better implementation
def binarysearch(sequence, value):
    lo, hi = 0, len(sequence) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sequence[mid] < value:
            lo = mid + 1
        elif value < sequence[mid]:
            hi = mid - 1
        else:
            return mid
    return None

#False
print binary_search(15, sorted_array, start, end)
print binary_search(2, sorted_array, start, end)
print binary_search(27, sorted_array, start, end)
#True
print binary_search(26, sorted_array, start, end)
print binary_search(31, sorted_array, start, end)
print binary_search(93, sorted_array, start, end)
print binary_search(17, sorted_array, start, end)
#False
print binary_search(94, sorted_array, start, end)
print binary_search(16, sorted_array, start, end)

print binary_search(0, [0], 0, 0)

