#!/usr/bin/python
# -*- coding: UTF-8 -*-

L = [1, 2, 3, 4, 5]
s1 = ','.join(str(n) for n in L)
print(s1)
print(L)

s2 = ''
for n in L:
    s2 += str(n) + ','
s2 = s2.rstrip(',')
print(s2)

