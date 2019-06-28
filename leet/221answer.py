#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/4/27 9:39 
# @Author : freelikeff 
# @Site : 
# @File : 221answer.py 
# @Software: PyCharm


# 传统动态规划
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        height = len(matrix)
        if not height:
            return 0
        width = len(matrix[0])
        if not width:
            return 0

        ans = [[0 for w in range(width)] for h in range(height)]

        # 先处理上边和左边
        for w in range(width):
            if matrix[0][w] == "1":
                ans[0][w] = 1
        for h in range(height):
            if matrix[h][0] == "1":
                ans[h][0] = 1

        # 开始规划
        for h in range(1, height):
            for w in range(1, width):
                if matrix[h][w] == "1":
                    ans[h][w] = min(ans[h - 1][w], ans[h][w - 1], ans[h - 1][w - 1]) + 1

        return (max([max(row) for row in ans]))**2      # 返回面积，所以要平方


if __name__ == '__main__':
    s = Solution()
    inpt = [["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]]
    answer = s.maximalSquare(inpt)
    print(answer)
