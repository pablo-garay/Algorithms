
def fibonacci(n):
    fib = [None] * (n + 1)
    fib[1] = fib[2] = 1

    for k in xrange(3, n + 1):
        fib[k] = fib[k - 1] + fib[k - 2]

    return fib[n]

print fibonacci(10)
print fibonacci(20)

