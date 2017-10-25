#!/bin/python

import sys

def t(n, arr, coins):
    sum = 0

    if n in coins:
        sum += 1

    for coin in coins:
        if n - coin > 0:
            sum += arr[n - coin]

    arr[n] = sum
    print "arr[%d] = %d" %(n, sum)


def make_change(coins, n):
    arr = [0] * (n + 1)
    set_coins = set(coins)

    for i in xrange(1, n + 1):  # include n, hence n + 1
        t(i, arr, set_coins)

    return arr[n]

# n, m = raw_input().strip().split(' ')
# n, m = [int(n), int(m)]
# coins = map(int, raw_input().strip().split(' '))
print make_change([1, 2, 3], 4)
