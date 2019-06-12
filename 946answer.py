#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 18:53
# @Author  : frelikeff
# @Site    : 
# @File    : 946answer.py
# @Software: PyCharm
from typing import List


class Solution:
    # 思路理清就行
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 设置一个暂存栈
        stack = []
        # 对入栈序列进行一个模拟
        for item in pushed:
            stack.append(item)
            # 如果暂存栈不空且栈顶既是出栈元素，那么出栈，并且在poped序列中也剔除
            while stack and stack[-1] == popped[0]:
                popped.pop(0)
                stack.pop()

        return not stack


if __name__ == '__main__':
    s = Solution()
    inpt = [2,1,0], [0,1,2]
    answer = s.validateStackSequences(*inpt)
    print(answer)
