#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 20:43
# @Author  : freelikeff
# @Site    : 
# @File    : 119answer.py
# @Software: PyCharm


class Solution(object):
    def getRow(self, numRows):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        numRows+=1
        if numRows == 0:
            return []
        if numRows == 1:
            return [1]
        front = [1, 1]
        if numRows == 2:
            return front

        for i in range(2, numRows):
            the = [1 for j in range(i + 1)]
            for k in range(1, i):
                the[k] = front[k - 1] + front[k]

            front = the
        return the