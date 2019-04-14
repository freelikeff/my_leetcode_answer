#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 20:48
# @Author  : freelikeff
# @Site    : 
# @File    : 165answer.py
# @Software: PyCharm
from itertools import zip_longest


class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        for i, j in zip_longest(v1, v2, fillvalue='0'):
            i, j = int(i), int(j)
            if i > j:
                return 1
            elif i < j:
                return -1
        return 0


if __name__ == "__main__":
    s = Solution()
    inpt = "1.1", "1.2.0"
    answer = s.compareVersion(*inpt)
    print(answer)
