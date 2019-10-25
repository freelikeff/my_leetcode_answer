#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 14:43
# @Author  : frelikeff
# @Site    : 
# @File    : 1124answer.py
# @Software: PyCharm
from typing import List


# 单调栈
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        if not hours:
            return 0

        if len(hours) == 1:
            return 1 if hours[0] > 8 else 0

        def sign(x):
            if x > 8:
                return 1
            return -1

        flags = [sign(item) for item in hours]
        presum = [0]
        for item in flags:
            presum.append(presum[-1] + item)

        decrease_stack = [0]  # 存放的是idx

        for i in range(1, len(presum)):
            if presum[i] < presum[decrease_stack[-1]]:
                decrease_stack.append(i)
        ans = 0
        i = len(hours)
        while i > ans:
            while decrease_stack and presum[decrease_stack[-1]] < presum[i]:
                ans = max(ans, i - decrease_stack[-1])
                decrease_stack.pop()
            i -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    inpt = [6, 6, 8]
    print(s.longestWPI(inpt))
