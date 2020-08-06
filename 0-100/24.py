#!/usr/bin/python
# -*- coding: UTF-8 -*-
from functools import reduce
a = 2.0
b = 1.0
s = 0
for n in range(1, 21):
    s += a / b
    t = a
    a = a + b
    b = t
print(s)

a = 2.0
b = 1.0
s = 0.0
for n in range(1, 21):
    s += a / b
    b, a = a, a + b
print(s)

s = 0.0
for n in range(1, 21):
    s += a / b
    b, a = a, a + b
print(s)


a = 2.0
b = 1.0
l = []
l.append(a / b)
for n in range(1,20):
    b,a = a,a + b
    l.append(a / b)
print(reduce(lambda x,y: x + y,l))
