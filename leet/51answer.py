#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/7 12:27
# @Author  : frelikeff
# @Site    : 
# @File    : 51answer.py
# @Software: PyCharm
from typing import List


# 正对角kidx=i+j,反对角tidx=i-j
def helper(n: int, cmemos, kmemos, tmemos, rest: int):
    if rest == 1:
        only_idx = sum(range(n)) - sum(cmemos)
        if only_idx + n - 1 not in kmemos and only_idx - n + 1 not in tmemos:
            return [[only_idx]]
        else:
            return None
    ans = []
    for i in range(n):
        if i not in cmemos and i + n - rest not in kmemos and i - n + rest not in tmemos:
            temp = helper(n, cmemos + [i], kmemos + [i + n - rest], tmemos + [i - n + rest], rest - 1)
            if temp:
                ans.extend([[i] + item for item in temp])
    return ans if ans else None


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = helper(n, [], [], [], n)
        if not output:
            return []
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in output]


if __name__ == '__main__':
    s = Solution()
    inpt = 2
    ans = s.solveNQueens(inpt)
    print(len(ans), ans)
