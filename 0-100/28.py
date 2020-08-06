#!/usr/bin/python
# -*- coding: UTF-8 -*-


def age(n):
    if n == 1:
        c = 10
    else:
        c = age(n - 1) + 2
    return c


print(age(5))

Age = 10
for index in range(0, 5):
    Age = 10 + index * 2

print(Age)
