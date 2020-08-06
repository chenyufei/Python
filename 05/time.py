#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)
localtime = time.asctime(time.localtime(time.time()))
print("本地时间为 :", localtime)

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%A %B %d %H:%M:%S %Y", time.localtime()))
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))


import calendar

cal = calendar.month(2016, 1)
print("以下输出2016年1月份的日历:")
print(cal)

cal = calendar.month(2019, 8)
print("以下输出2019年8月份的日历:")
print(cal)

cal = calendar.month(2019, 9)
print("以下输出2019年9月份的日历:")
print(cal)

cal = calendar.month(2019, 10)
print("以下输出2019年10月份的日历:")
print(cal)

print(calendar.monthrange(2019, 10))


def ChangeInt(a):
    a = 10


b = 2
ChangeInt(b)
print(b)  # 结果是 2


# 可写函数说明
def changeme(mylist):
    # "修改传入的列表"
    mylist.append(40)
    mylist.append(50)
    mylist.append([1, 2, 3, 4]);
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print("函数外取值: ", mylist)


# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)

# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))

total = 0;  # 这是一个全局变量


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


# 调用sum函数
sum(10, 20);
print("函数外是全局变量 : ", total)


try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()
