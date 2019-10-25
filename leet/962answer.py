#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 17:00
# @Author  : frelikeff
# @Site    : 
# @File    : 962answer.py
# @Software: PyCharm

from typing import List
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        if len(A)<2:
            return 0
        decrease_stack=[0]
        for i in range(1,len(A)):
            if A[i]<=A[decrease_stack[-1]]:
                decrease_stack.append(i)

        ans=0
        i=len(A)-1
        while i>ans:
            while decrease_stack and A[decrease_stack[-1]]<=A[i]:
                ans=max(ans,i-decrease_stack[-1])
                decrease_stack.pop()
            i-=1
        return ans


if __name__ == '__main__':
    s=Solution()
    inpt=[6,0,8,2,1,5]
    print(s.maxWidthRamp(inpt))
