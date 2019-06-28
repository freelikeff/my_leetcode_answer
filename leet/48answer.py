#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 22:03
# @Author  : freelikeff
# @Site    : 
# @File    : 48answer.py
# @Software: PyCharm


# 这是自己的答案，四个数字一组进行旋转，两层循环，表示层数和顺序
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range((n + 1) // 2):
            for j in range(n // 2):
                matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = \
                matrix[n - 1 - j][i], matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j]


# 看到别人注释nb，我也想说，nb
# 对于方阵旋转90°，其实就是方阵上下反转然后转置 （当然，对于方阵逆时针旋转90°，则是先转置然后上下翻转）
# map 函数对可迭代对象实现func，将结果打爆列表返回
# zip函数，对一系列可迭代对象，将对象中对应的元素打包成一个个元组，返回列表
# *这个符号用于解包
# 但其实不是就地的，小瑕疵
class Solution2:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = map(list, zip(*matrix[::-1]))


if __name__ == "__main__":
    s=Solution2()
    inpt=[[1,2,3],  [4,5,6], [7,8,9]]
    s.rotate(inpt)
    print(inpt)