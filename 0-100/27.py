#!/usr/bin/python
# -*- coding: UTF-8 -*-


def output(srcstr, length):
    if length == 0:
        return
    print(srcstr[length - 1], end='')
    output(srcstr, length - 1)


srcstr = input('Input a string:')
length = len(srcstr)
output(srcstr, length)
