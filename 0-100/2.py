#!/usr/bin/python
# -*- coding: UTF-8 -*-


def calculate(num):
    if num > 1000000:
        print("超出100万的提成:%.2f" % ((num - 1000000) * 0.01))
        calculate(1000000)
    elif num > 600000:
        print("超出60万的提成:%.2f" % ((num-600000) * 0.015))
        calculate(600000)
    elif num > 400000:
        print("超出40万的提成:%.2f" % ((num - 400000) * 0.03))
        calculate(400000)
    elif num > 200000:
        print("超出20万的提成:%.2f" % ((num - 200000) * 0.05))
        calculate(200000)
    elif num > 100000:
        print("超出10万的提成:%.2f" % ((num - 100000) * 0.075))
        calculate(100000)
    else:
        print("低于10万的提成:%.2f" % (num * 0.1))


def calculate_one(num):
    if num > 1000000:
        print("超出100万的提成:%.2f" % ((num - 1000000) * 0.01))
        print("超出60万的提成:%.2f" % ((1000000 - 600000) * 0.015))
        print("超出40万的提成:%.2f" % ((600000 - 400000) * 0.03))
        print("超出20万的提成:%.2f" % ((400000 - 200000) * 0.05))
        print("超出10万的提成:%.2f" % ((200000 - 100000) * 0.075))
        print("低于10万的提成:%.2f" % (100000 * 0.1))
    elif num > 600000:
        print("超出60万的提成:%.2f" % ((num-600000) * 0.015))
        print("超出40万的提成:%.2f" % ((600000 - 400000) * 0.03))
        print("超出20万的提成:%.2f" % ((400000 - 200000) * 0.05))
        print("超出10万的提成:%.2f" % ((200000 - 100000) * 0.075))
        print("低于10万的提成:%.2f" % (100000 * 0.1))
    elif num > 400000:
        print("超出40万的提成:%.2f" % ((num - 400000) * 0.03))
        print("超出20万的提成:%.2f" % ((400000 - 200000) * 0.05))
        print("超出10万的提成:%.2f" % ((200000 - 100000) * 0.075))
        print("低于10万的提成:%.2f" % (100000 * 0.1))
    elif num > 200000:
        print("超出20万的提成:%.2f" % ((num - 200000) * 0.05))
        print("超出10万的提成:%.2f" % ((200000 - 100000) * 0.075))
        print("低于10万的提成:%.2f" % (100000 * 0.1))
    elif num > 100000:
        print("超出10万的提成:%.2f" % ((num - 100000) * 0.075))
        print("低于10万的提成:%.2f" % (100000 * 0.1))
    else:
        print("低于10万的提成:%.2f" % (num * 0.1))


def calculate_two(num):
    arr = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0
    i = int(str)
    for idx in range(0, 6):
        if i > arr[idx]:
            r += (i - arr[idx]) * rat[idx]
            print((i - arr[idx]) * rat[idx])
            i = arr[idx]
    print(r)


if __name__ == '__main__':
    str = input("请输入年利润:")
    calculate(int(str))
    calculate_one(int(str))
    calculate_two(int(str))

