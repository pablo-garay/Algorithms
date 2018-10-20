# Remember this is for Python3
t = int(input().rstrip())

for iteration in range(t):
    n = int(input().rstrip())
    array = map(int, input().rstrip().split())

    # print t, n, arr
    array = sorted(array)

    i = 1
    while i <= (n - 1):
        aux = array[i]
        array[i] = array[i - 1]
        array[i - 1] = aux
        i += 2

    print(" ".join(map(str, array)))
