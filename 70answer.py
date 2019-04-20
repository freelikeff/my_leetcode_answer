#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 10:47
# @Author  : freelikeff
# @Site    : 
# @File    : 70answer.py
# @Software: PyCharm

from functools import lru_cache


# 递归，Fibonacci.看起来简单，实际上time over，memory over，所以递归轻易不要用,就这还算是尾递归，这谁顶得住
# 加上缓存还是很慢，还不如开个数组
class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution1:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n

        a, b, i = 2, 3, 4
        while i <= n:
            a = a + b
            a, b = b, a
            i += 1

        return b


if __name__ == '__main__':
    s = Solution1()
    inpt = 50  # 20365011074
    answer = s.climbStairs(inpt)
    print(answer)
