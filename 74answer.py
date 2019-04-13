#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 9:42
# @Author  : freelikeff
# @Site    : 
# @File    : 74answer.py
# @Software: PyCharm


# 其实相当于一个二维的二分查找，做左下或者右上都可以开始，例从右上，那么target>this，则this下移，反之左移
# 个人做了一点优化，但是好像没什么卵用，当target<this时，其实在当行进行二分查找就可以了，不用一直往左移
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None:
            return False

        if target > matrix[-1][-1]:
            return False

        height, width = len(matrix), len(matrix[0])
        i, j = 0, width - 1
        while i < height or j >= 0:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                break
        else:
            return False

        from bisect import bisect
        insert = bisect(matrix[i][:j], target)
        return target == matrix[i][insert-1]


if __name__ == "__main__":
    s = Solution()
    inpt = matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]],5
    answer = s.searchMatrix(*inpt)
    print(answer)
