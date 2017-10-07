
def mergesort(array, start, end):
    # print start, end
    if (start + 1) >= end:
        return
    else:
        half = (start + end) / 2  # e.g. for 9 it's 4
        mergesort(array, start, half)
        mergesort(array, half, end)

        temp_array = []
        i, j = start, half

        while i < half or j < end:
            if i == half:
                temp_array.append(array[j])
                j += 1
            elif j == end:
                temp_array.append(array[i])
                i += 1
            else:
                if array[i] > array[j]:
                    temp_array.append(array[i])
                    i += 1
                else:
                    temp_array.append(array[j])
                    j += 1

        array[start:end] = temp_array


def merge_sort(array):
    mergesort(array, 0, len(array))


for array in ([54,26,93,17,77,31,44,55,20],
              [54,26,93,17,77,31,44,55,20, 40]):
    print "Array before: ", array, "Length: ", len(array)
    merge_sort(array)
    print array
