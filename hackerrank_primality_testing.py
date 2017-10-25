import math


def check_prime(n):
    if n == 1:
        print("Not prime")
        return

    if n != 2 and n % 2 == 0:
        print("Not prime")
        return

    last = int(math.sqrt(n))

    for divisor in range(3, last + 2, 2):
        if n % divisor == 0:
            print("Not prime")
            return

    print("Prime")


p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    check_prime(n)
