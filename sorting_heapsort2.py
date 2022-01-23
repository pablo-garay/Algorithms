arr = [5, 2, 5, 6, 26, 7, 8, 9, 2, 1, 2, -1, 3]

from heapq import *
def heapsort(arr):  # Time: O(n log n). Space: O(n) total
    arr2 = []
    heapify(arr)  # O(n)
    while arr:  # O(n)
        arr2.append(heappop(arr))  # O(log n)
    arr[:] = arr2


print arr; heapsort(arr); print arr
