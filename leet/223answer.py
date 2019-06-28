#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 14:47
# @Author  : freelikeff
# @Site    : 
# @File    : 223answer.py
# @Software: PyCharm


# 要求的是并集，那么用面积之和减去并集就好了
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        return (C - A) * (D - B) + (H - F) * (G - E) - max(0, min(C - E, G - A, G - E, C - A)) * max(0,
                                                                                                     min(H - F, D - B,
                                                                                                         H - B, D - F))


if __name__ == "__main__":
    s = Solution()
    inpt = -3, 0, 3, 4, 0, -1, 9, 2
    answer = s.computeArea(*inpt)
    print(answer)
