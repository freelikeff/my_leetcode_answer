#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 16:24
# @Author  : frelikeff
# @Site    : 
# @File    : 85answer.py
# @Software: PyCharm
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        nums = [int(''.join(row), base=2) for row in matrix]
        print(nums)
        ans, N = 0, len(nums)
        for i in range(N):
            j, num = i, nums[i]
            while j < N:
                num = num & nums[j]
                if not num:
                    break
                l, curnum = 0, num
                while curnum:
                    l += 1
                    curnum = curnum & (curnum << 1)
                ans = max(ans, l * (j - i + 1))
                j += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    inpt = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    answer = s.maximalRectangle(inpt)
    print(answer)
