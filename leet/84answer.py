#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 11:26
# @Author  : frelikeff
# @Site    : 
# @File    : 84answer.py
# @Software: PyCharm
from typing import List
import pysnooper

# 单调栈
class Solution:
    @pysnooper.snoop()
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        # stack存的是index
        stack = []
        area = 0
        i = 0
        while i < len(heights):
            if not len(stack) or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i+=1
            else:
                j = stack.pop()
                temp = heights[j] * (i if not stack else i - stack[-1] - 1)
                if temp>area:
                    area=temp
        return area

if __name__ == "__main__":
    s = Solution()
    inpt = [3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    answer = s.largestRectangleArea(inpt)
    print(answer)
    print(inpt)
