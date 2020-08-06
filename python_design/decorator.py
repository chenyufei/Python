class foo(object):
    def f1(self):
        print("func f1")

    def f2(self):
        print("func f2")


class foo_decorator(object):
    def __init__(self, decorator):
        self._decorator = decorator

    def f1(self):
        print("decorator f1")
        self._decorator.f1()

    def __getattr__(self, item):
        # 当得不到想要的属性时,就去自己的装饰里面拿,使用 getattr()内建方法
        print(item)
        return getattr(self._decorator, item)


if __name__ == '__main__':
    # 主要思想还是使用魔法方法 __getattr__ 方法, 然后把另外一个对象赋值到自身的属性上面.
    # 添加一个运行另外一个对象的接口,没有接口时,就去直接调用另一个对象的方法.
    u = foo()
    d = foo_decorator(u)
    d.f1()
    d.f2()
