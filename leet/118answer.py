#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 20:13
# @Author  : freelikeff
# @Site    : https://leetcode-cn.com/problems/pascals-triangle/
# @File    : 118answer.py
# @Software: PyCharm


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        ans=[[1], [1, 1]]
        if numRows == 2:
            return ans

        for i in range(2, numRows):
            the = [1 for j in range(i + 1)]
            for k in range(1, i):
                the[k] = ans[i - 1][k - 1] + ans[i - 1][k]
            ans.append(the)
        return ans


if __name__ == '__main__':
    s = Solution()
    inpt = 3
    answer = s.generate(inpt)
    print(answer)
