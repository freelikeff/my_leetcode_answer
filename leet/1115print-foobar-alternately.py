#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 22:30
# @Author  : frelikeff
# @Site    : 
# @File    : 1115print-foobar-alternately.py
# @Software: PyCharm
import threading
class FooBar:
    def __init__(self, n):
        self.n = n
        self.fooSemaphore=threading.Semaphore(1)
        self.barSemaphore = threading.Semaphore(0)


    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.fooSemaphore.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()

            self.barSemaphore.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.barSemaphore.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.fooSemaphore.release()