arr = [5, 2, 5, 6, 26, 7, 8, 9, 2, 1, 2, 3]

def mergesort(arr, start, end):
    if start == end:
        return

    mid = (start + end + 1) / 2
    mergesort(arr, start, mid - 1); mergesort(arr, mid, end)

    left, right = (start, mid); ordered = []
    while left <= mid - 1 and right <= end:
        if arr[left] <= arr[right]:
            ordered.append(arr[left])
            left += 1
        else:
            ordered.append(arr[right])
            right += 1

    while left <= mid - 1:
        ordered.append(arr[left])
        left += 1
    while right <= end:
        ordered.append(arr[right])
        right += 1

    arr[start:end + 1] = ordered


mergesort(arr, 0, len(arr) - 1)
