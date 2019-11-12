#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 15:08
# @Author  : frelikeff
# @Site    : 
# @File    : 382answer.py
# @Software: PyCharm
from utils.makelinklist import ListNode

import random


class ReservoirSampling:
    def __init__(self):  #
        self._pool = None
        self._length = 1  # 给新进入流的item准备好的idx
        return

    def additem(self, item):
        if self._pool is None:
            self._pool = item
        else:
            probability = random.random()
            if probability <= 1 / self._length:
                self._pool = item

        self._length += 1
        return

    @property
    def pool(self):
        return self._pool

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.memo=head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        RS=ReservoirSampling()
        node=self.memo
        while node:
            RS.additem(node)
            node=node.next

        return RS.pool.val

