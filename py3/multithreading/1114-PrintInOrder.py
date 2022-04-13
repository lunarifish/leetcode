# 2022-4-13
# Runtime 3316ms(9.3%)
# Memory 15.2ms(91.0%)

##
# 赶快学用线程锁！！
###

class Foo:
    def __init__(self):
        pass
    status = [False, False]
    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        Foo.status[0] = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        while not Foo.status[0]: pass
        printSecond()
        Foo.status[1] = True


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        while not Foo.status[1]: pass
        printThird()
        Foo.status = [False, False]
