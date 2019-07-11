#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 10:20
# @Author  : frelikeff
# @Site    : 
# @File    : 96answer.py
# @Software: PyCharm

# 递归顺手了，都忘了递归的效率了。。。
class Solution:
    def numTrees(self, n: int) -> int:
        if n < 2:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        ans = 0
        for i in range(n):
            ans += self.numTrees(i) * self.numTrees(n - 1 - i)
        return ans


# 老老实实动态规划走一波
class Solution2:
    def numTrees(self, n: int) -> int:
        if n < 2:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        ans = [0] * (n+1)
        ans[0], ans[1], ans[2], ans[3] = 1, 1, 2, 5
        for k in range(4, n+1):
            for i in range(k):
                ans[k] += ans[i] * ans[k - 1 - i]
        return ans[-1]


if __name__ == '__main__':
    s = Solution2()
    for i in range(100):
        print(s.numTrees(i))
