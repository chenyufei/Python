class A(object):
    def __foo(self, x):
        print("executing _foo(%s,%s)" %(self, x))
        print('self:', self)
    def chen(self):
        __foo(5)
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)

a = A()
print(a.chen)
print(a.class_foo)
print(a.static_foo)

a.chen()
A.class_foo(a,4)
A.static_foo(8)

