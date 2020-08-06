class A(object):
    __obj = False
    __init = False

    def __init__(self, name):
        print("__init__")
        if not A.__init:
            self.name = name
            A.__init = True

    def __new__(cls, *args, **kwargs):
        print("__new__")
        if not A.__obj:
            A.__obj = super().__new__(cls)
        return A.__obj


if __name__ == '__main__':
    # 只初始化一次的单例模式
    a = A("nick")
    b = A("nick2")
    print(a.name)  # nick
    print(b.name)  # nick
    print(a == b)  # True
    print(id(a), id(b))  # 54527760 54527760
