#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 9:42
# @Author  : freelikeff
# @Site    : 
# @File    : 63answer.py
# @Software: PyCharm


# 动态规划，每个地方只能从左边或者上边来，那么到这个点的途径就等于左边+右边
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid): # TODO(freelikeff): 能否利用dfs？
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        ans_matrix = [[0 for i in range(width)] for i in range(height)]

        # 初始化第一行第一列
        for i in range(width):
            if obstacleGrid[0][i]:
                break
            ans_matrix[0][i] = 1

        for i in range(height):
            if obstacleGrid[i][0]:
                break
            ans_matrix[i][0] = 1

        # 开始动态规划
        for i in range(1, height):
            for j in range(1, width):
                if not obstacleGrid[i][j]:
                    ans_matrix[i][j] = ans_matrix[i - 1][j] + ans_matrix[i][j - 1]

        return ans_matrix[-1][-1]


if __name__ == "__main__":
    s = Solution()
    inpt = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    answer = s.uniquePathsWithObstacles(inpt)
    print(answer)
