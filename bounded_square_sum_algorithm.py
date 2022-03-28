from bisect import *
def f(a, b, lower, upper):  # Time: O(n log n)
    num = 0
    for i in xrange(len(a)): a[i] *= a[i]
    for i in xrange(len(b)): b[i] *= b[i]
    a.sort(); b.sort()  # O(n log n)

    for i in xrange(len(b)):  # O(n log n)
        left = lower - b[i]; right = upper - b[i]
        i1 = bisect_left(a, left); i2 = bisect_right(a, right)  # this line only: O(log n)

        if i1 == i2:
            # print left, right, a, None
            continue
        else:
            if i2 == len(a) or right < b[i2]:
                i2 -= 1

            num += (i2 - i1) + 1
            # print left, right, a, i1, i2
            # print (i2 - i1) + 1

    return num


print f(a = [3, -1, 9], b = [100, 5, -2], lower = 7, upper = 99)
print f(a = [1, 2, 3, -1, -2, -3], b = [10], lower = 0, upper = 100)
print f(a = [1, 2, 3, -1, -2, -3], b = [1], lower = 100, upper = 1000)
