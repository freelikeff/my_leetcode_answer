#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/10 9:16
# @Author  : frelikeff
# @Site    : 
# @File    : 841answer.py
# @Software: PyCharm
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        memoset = {0}
        stack = rooms[0]
        while stack:
            key = stack.pop()
            memoset.add(key)
            for cankey in rooms[key]:
                if cankey not in memoset:
                    stack.append(cankey)
        return len(memoset) == len(rooms)


