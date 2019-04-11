#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 15:19
# @Author  : freelikeff
# @Site    : 
# @File    : 60answer.py
# @Software: PyCharm

from itertools import permutations


# 使用的内置模块itertools
class Solution:

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        a = permutations(range(1, n + 1))

        rank = 1
        while rank < k:
            rank += 1
            next(a)

        return "".join([str(item) for item in next(a)])


# 一位一位的确定，然后输出
class Solution2:
    def getPermutation(self, n: 'int', k: 'int') -> 'str':
        ans = ''
        k -= 1
        fac = 1
        for i in range(1, n):  # 第一位确定时的全排列数量
            fac *= i
        print(fac)
        num = [str(i + 1) for i in range(n)]
        print(num)
        for i in reversed(range(n)):
            curr = num[k // fac]  # 下标是k//fac的数字
            ans += str(curr)
            num.remove(curr)  # 使用过的数字移除
            if i != 0:
                k %= fac
                fac = fac // i  # 再固定一位时候的全排列数量
        return ans


if __name__ == "__main__":
    s = Solution2()
    inpt = 3, 3
    answer = s.getPermutation(*inpt)
    print(answer)
