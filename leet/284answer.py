#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 16:36
# @Author  : frelikeff
# @Site    : 
# @File    : 284answer.py
# @Software: PyCharm

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        if self.iterator.hasNext():
            self.memo = self.iterator.next()
        else:
            self.memo = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.memo

    def next(self):
        """
        :rtype: int
        """
        ans = self.memo
        if self.iterator.hasNext():
            self.memo = self.iterator.next()
        else:
            self.memo = None
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.memo is not None
