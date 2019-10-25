#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 13:43
# @Author  : frelikeff
# @Site    : 
# @File    : 335answer.py
# @Software: PyCharm
from typing import List


class Solution:
    def isSelfCrossing(self, x) -> bool:
        if len(x) < 4:
            return False
        if len(x) == 4:
            return True if x[3] >= x[1] and x[2] <= x[0] else False
        for i in range(3, len(x)):
            if x[i] >= x[i - 2] and x[i - 1] <= x[i - 3]:
                return True
            if i > 3 and x[i - 1] == x[i - 3] and x[i - 4] + x[i] >= x[i - 2]:
                return True
            if i > 4 and x[i - 3] - x[i - 5] <= x[i - 1] <= x[i - 3] and x[i - 2] - x[i - 4] <= x[i] <= x[i - 2] and x[
                i - 2] > x[i - 4]:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    inpt = [3, 3, 4, 2, 2]
    print(s.isSelfCrossing(inpt))
