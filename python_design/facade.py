class SmallOrPieceOne:
    def __init__(self):
        pass

    def do_small1(self):
        print('do small 1')


class SmallOrPieceTwo:
    def __init__(self):
        pass

    def do_small2(self):
        print('do small 2')


class SmallOrPieceThree:
    def __init__(self):
        pass

    def do_small3(self):
        print('do small 3')


class Outside:
    def __init__(self):
        self.__small1 = SmallOrPieceOne()
        self.__small2 = SmallOrPieceTwo()
        self.__small3 = SmallOrPieceThree()

    def method1(self):
        self.__small1.do_small1()  # 如果这里调用的不只2两函数，作用就显示出来了，可以把原本复杂的函数调用关系清楚化，统一化
        self.__small2.do_small2()

    def method2(self):
        self.__small2.do_small2()
        self.__small3.do_small3()


if __name__ == '__main__':
    # 外观模式应用于在很多复杂而小功能需要调用时,并且这些调用还具有一定的相关性,即一调用就是一系列的调用.
    osd = Outside()
    osd.method1()
    osd.method2()
