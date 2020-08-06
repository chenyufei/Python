#!/usr/bin/python
# -*- coding: UTF-8 -*-

def num(n):
    i = n // 100
    j = n // 10 % 10
    k = n % 10
    #print('%d %d %d %d' % (n, i, j, k))
    #print('%d %d %d' % (i**3, j**3, k**3))
    if n == i ** 3 + j ** 3 + k ** 3:
        print(n)


for n in range(112, 1000):
    num(n)
