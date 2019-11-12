#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 9:11
# @Author  : frelikeff
# @Site    : 
# @File    : 295answer.py
# @Software: PyCharm
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxheap, self.frontsize = [], 0
        self.minheap, self.backsize = [], 0

    # 保证 self.backsize-self.frontsize==0 or 1
    def addNum(self, num: int) -> None:
        if not self.backsize:
            heapq.heappush(self.minheap, num)
            self.backsize += 1
            return

        if self.backsize == self.frontsize:  # 两段长度相等
            if num >= -self.maxheap[0]:
                heapq.heappush(self.minheap, num)

            else:

                heapq.heappush(self.minheap, -heapq.heappushpop(self.maxheap, -num))

            self.backsize += 1
        else:  # 后面比前面长1
            if num <= self.minheap[0]:
                heapq.heappush(self.maxheap, -num)

            else:

                heapq.heappush(self.maxheap, -heapq.heappushpop(self.minheap, num))

            self.frontsize += 1

    def findMedian(self) -> float:
        if self.backsize == self.frontsize:
            return (-self.maxheap[0] + self.minheap[0]) / 2
        return self.minheap[0]


if __name__ == '__main__':
    s = MedianFinder()
    s.addNum(1)
    s.addNum(2)

    print(s.maxheap, s.frontsize, s.minheap, s.backsize,s.findMedian())
