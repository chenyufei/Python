#!/usr/bin/python
# -*- coding: UTF-8 -*-


def Fibonacci(num):
    a, b = 1, 1
    for index in range(num-1):
        a, b = b, a+b
    return a


def Fibonacci_callback(num):
    if num == 1 or num == 2:
        return 1
    return Fibonacci_callback(num-1) + Fibonacci_callback(num-2)


def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


if __name__ == '__main__':
    num = input("请输入斐波那契数列的列数:\n")
    print(Fibonacci(int(num)))
    print(Fibonacci_callback(int(num)))
    print(fib(int(num)))

