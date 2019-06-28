#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 10:26
# @Author  : freelikeff
# @Site    : 
# @File    : 64answer.py
# @Software: PyCharm


# 感觉还是可以用动态规划来做，每个位置的best应该是min（左best，上best）+这个位置
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        width = len(grid[0])
        ans_matrix = [[0 for i in range(width)] for i in range(height)]
        ans_matrix[0][0] = grid[0][0]
        # 初始化第一行第一列
        for i in range(1, width):
            ans_matrix[0][i] = ans_matrix[0][i - 1] + grid[0][i]

        for i in range(1, height):
            ans_matrix[i][0] = ans_matrix[i - 1][0] + grid[i][0]

        # 开始动态规划
        for i in range(1, height):
            for j in range(1, width):
                ans_matrix[i][j] = min(ans_matrix[i - 1][j], ans_matrix[i][j - 1]) + grid[i][j]

        return ans_matrix[-1][-1]


if __name__ == "__main__":
    s = Solution()
    inpt = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    answer = s.minPathSum(inpt)
    print(answer)
