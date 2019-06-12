#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 20:42
# @Author  : frelikeff
# @Site    : 
# @File    : 509answer.py
# @Software: PyCharm

from functools import lru_cache
import numpy as np


# 简单递归
@lru_cache()
class Solution:
    def fib(self, n: int) -> int:
        assert n >= 0
        return 1 if n < 2 else self.fib(n - 1) + self.fib(n - 2)


# 循环
class Solution2:
    def fib(self, n: int) -> int:
        assert n >= 0
        if n < 2:
            return 1
        second = 1
        ans = 2
        for i in range(n - 2):
            first, second = second, ans
            ans = first + second

        return ans


# 矩阵幂
def mat_pow(mat: np.ndarray, pow) -> np.ndarray:
    if pow == 1:
        return mat
    if pow == 2:
        return np.dot(mat, mat)
    if pow & 1:
        return np.dot(mat_pow(mat_pow(mat, pow // 2), 2), mat)
    else:
        return mat_pow(mat_pow(mat, pow // 2), 2)

# 出现了溢出问题
class Solution3:
    def fib(self, n: int) -> int:
        assert n >= 0
        if n < 2:
            return 1
        return mat_pow(np.array([[1,1],[1,0]]),n)[0][0]


if __name__ == '__main__':
    s = Solution3()
    q=Solution2()
    for item in range(100):
        print(s.fib(item),"-->",q.fib(item))
