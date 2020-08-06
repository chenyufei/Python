#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : %s, Salary:" % self.name, self.salary)


# "创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
# "创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

if hasattr(emp1, 'age'):    # 如果存在 'age' 属性返回 True。
    getattr(emp1, 'age')    # 返回 'age' 属性的值
else:
    setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
    getattr(emp1, 'age')    # 返回 'age' 属性的值
delattr(emp1, 'age')    # 删除属性 'age'


print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()


class Test1:
    def prt(runobj):
        print(runobj)
        print(runobj.__class__)

t = Test1()
t.prt()


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")


pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))  # 打印对象的id
del pt1
del pt2
del pt3


class Parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print('调用父类方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性 :", Parent.parentAttr)


class Child(Parent):  # 定义子类
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print('调用子类方法')


c = Child()  # 实例化子类
c.childMethod()  # 调用子类的方法
c.parentMethod()  # 调用父类方法
c.setAttr(200)  # 再次调用父类的方法 - 设置属性值
c.getAttr()  # 再次调用父类的方法 - 获取属性值


class Parent:  # 定义父类
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
try:
    print(counter.__secretCount)  # 报错，实例不能访问私有变量
except Exception as e:
    print(e)

print(counter._JustCounter__secretCount)  # Python不允许实例化的类访问私有数据，但你可以使用
                                          #  object._className__attrName（ 对象名._类名__私有属性名 ）
                                          # 访问属性
print("==========")

#  单下划线、双下划线、头尾双下划线说明
#  __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的
# _foo: 以单下划线开头的表示的是 protected 类型的变量，
# 即保护类型只能允许其本身与子类进行访问，不能用于 from module import
# __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了
