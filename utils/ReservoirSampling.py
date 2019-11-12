#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 10:42
# @Author  : frelikeff
# @Site    : 
# @File    : ReservoirSampling.py
# @Software: PyCharm
import random


class ReservoirSampling:
    def __init__(self, poolsize: int):
        self._pool = []
        self._poolsize = poolsize
        self._length = 1  # 给新进入流的item准备好的idx
        return

    def additem(self, item):
        # 如果池子没满，那么直接加入池子
        if self._length <= self._poolsize:
            self._pool.append(item)

        # 满了的话就要按照蓄水池算法进行替换
        else:
            probability = random.random()
            if probability <= self._poolsize / self._length:
                choosed = random.randint(0, self._poolsize - 1)
                self._pool[choosed] = item

        self._length += 1

    # 查看池子
    @property
    def pool(self):
        return self._pool


if __name__ == '__main__':
    mypool = ReservoirSampling(3)
    for i in range(8):
        mypool.additem(i)
        print(mypool.pool)
