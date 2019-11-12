#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 15:22
# @Author  : frelikeff
# @Site    : 
# @File    : 470answer.py
# @Software: PyCharm
import random


def rand7():
    return random.randint(1, 7)


class Solution1:
    def rand10(self):
        """
        :rtype: int
        """
        a = 7
        while a > 5:
            a = rand7()

        b = 7
        while b == 7:
            b = rand7()

        return 5*(b&1)+a



