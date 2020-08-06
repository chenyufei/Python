#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    lsort = []
    for index in range(0,3):
        num = input("请输入第数字:\n")
        lsort.append(int(num))
    lsort.sort()
    print(lsort)
    