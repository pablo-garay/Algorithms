#!/bin/python

import sys
import os


def triangleOrNot(a, b, c):  # O(n) where n: num of triangles given as input
    res = []
    for n in xrange(len(a)):
        if a[n] < (b[n] + c[n]) and b[n] < (a[n] + c[n]) and c[n] < (a[n] + b[n]):
            res.append("Yes")
        else:
            res.append("No")

    return res

if __name__ == "__main__":
    a = []
    b = []
    c = []

    num_tris = int(raw_input())
    for i in xrange(num_tris):
        a.append(int(raw_input()))

    num_tris = int(raw_input())
    for i in xrange(num_tris):
        b.append(int(raw_input()))

    num_tris = int(raw_input())
    for i in xrange(num_tris):
        c.append(int(raw_input()))

    for n in xrange(num_tris):
        print triangleOrNot(a[n], b[n], c[n])
