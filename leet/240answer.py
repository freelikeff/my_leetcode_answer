#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/4/25 20:36 
# @Author : freelikeff 
# @Site : 
# @File : 240answer.py 
# @Software: PyCharm


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        height, width = len(matrix), len(matrix[0])
        i, j = height - 1, 0
        while i >= 0 and j < width:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False

class Solution1:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if target in row:
                return True
        return False

if __name__ == "__main__":
    s = Solution()
    inpt = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    answer = s.searchMatrix(inpt, 16)
    print(answer)
