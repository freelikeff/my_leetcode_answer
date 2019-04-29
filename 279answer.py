#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/4/25 9:23 
# @Author : freelikeff 
# @Site : 
# @File : 279answer.py 
# @Software: PyCharm


# 四平方定理。任何一个正整数都可以表示成不超过四个整数的平方之和。 推论：满足四数平方和定理的数n（四个整数的情况），必定满足 n=4^a(8b+7)
# 先把四的次方消掉，然后如果除以八余7，那么return 4.接下来一个平方数一个平方数的试，如果恰好等于两个平方数的和（返回这俩不为零的个数）
# 如果不存在，呢么返回 3.我瞎了，你呢
class Solution:
    def numSquares(self, n: int) -> int:  # TODO(freelikeff): 背包问题，最短路径

        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        a = 0
        while a ** 2 <= n:
            b = int((n - a ** 2) ** 0.5)
            if a ** 2 + b ** 2 == n:
                return (not not a) + (not not b)
            a += 1
        return 3


# 动态规划,时间超了，空间估计也不小
class Solution2:
    def numSquares(self, n: int):

        """
        :type n: int
        :rtype: int
        """
        ans=[0 for i in range(n+1)]

        for i in range(1, n + 1):
            the_sqrt = int(i ** 0.5)
            if int(the_sqrt) ** 2 == i:
                ans[i] = 1
                continue


            minn = 4
            for k in range(1, the_sqrt + 1):
                minn = min(ans[i - k ** 2], minn)

            ans[i] = minn + 1

        return ans[-1]


if __name__ == '__main__':
    s = Solution2()
    inpt = 8285
    answer = s.numSquares(inpt)
    print(answer)
