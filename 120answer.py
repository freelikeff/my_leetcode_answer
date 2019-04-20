#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 20:55
# @Author  : freelikeff
# @Site    : 
# @File    : 120answer.py
# @Software: PyCharm


# 动态规划，可优化
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        ans = [[0] * (i + 1) for i in range(len(triangle))]
        ans[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):  # 每一行做处理,每行有i+1个元素

            ans[i][0] = ans[i - 1][0]+triangle[i][0]
            ans[i][-1]=ans[i - 1][-1]+triangle[i][-1]

            for k in range(1,i):
                ans[i][k] = min(ans[i - 1][k - 1], ans[i - 1][k])+triangle[i][k]

        return min(ans[-1])


class Solution2(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        ans=[triangle[0][0]]
        for i in range(1, len(triangle)):  # 每一行做处理,每行有i+1个元素
            the=[0]*(i+1)
            the[0] = ans[0] + triangle[i][0]
            the[-1] = ans[-1] + triangle[i][-1]

            for k in range(1, i):
                the[k] = min(ans[k - 1], ans[k]) + triangle[i][k]

            ans=the
        return min(ans)


if __name__ == '__main__':
    s = Solution2()
    inpt = [[2],[3,4],[6,5,7],[4,1,8,3]]
    answer = s.minimumTotal(inpt)
    print(answer)
