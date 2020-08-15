#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 10:13
# @Author  : frelikeff
# @Site    : 
# @File    : MagicCube.py
# @Software: PyCharm


class MagicCube:
    def __init__(self):  # udfblr 上下前后左右
        self.state = [[1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3],
                      [4, 4, 4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6, 6]]

    def right(self):
        self.state[2][0], self.state[2][2], self.state[2][7], self.state[2][5] = self.state[2][5], self.state[2][0], \
                                                                                 self.state[2][2], self.state[2][7]
        self.state[2][1], self.state[2][4], self.state[2][6], self.state[2][3] = self.state[2][3], self.state[2][1], \
                                                                                 self.state[2][4], self.state[2][6]
        self.state[0][2], self.state[4][2], self.state[3][2], self.state[1][2] = self.state[1][2], self.state[0][2],self.state[4][2], self.state[3][2]
        self.state[0][7], self.state[4][7], self.state[3][7], self.state[1][7] = self.state[1][7], self.state[0][7],self.state[4][7], self.state[3][7]
        self.state[0][4], self.state[4][4], self.state[3][4], self.state[1][4] = self.state[1][4], self.state[0][4], \
                                                                                 self.state[4][4], self.state[3][4]

    def left(self):
        self.state[5][0], self.state[5][2], self.state[5][7], self.state[5][5] = self.state[5][5], self.state[5][0], \
                                                                                 self.state[5][2], self.state[5][7]
        self.state[5][1], self.state[5][4], self.state[5][6], self.state[5][3] = self.state[5][3], self.state[5][1], \
                                                                                 self.state[5][4], self.state[5][6]
        self.state[0][5], self.state[4][5], self.state[3][5], self.state[1][5] = self.state[1][5], self.state[0][5], \
                                                                                 self.state[4][5], self.state[3][5]
        self.state[0][0], self.state[4][0], self.state[3][0], self.state[1][0] = self.state[1][0], self.state[0][0], \
                                                                                 self.state[4][0], self.state[3][0]
        self.state[0][3], self.state[4][3], self.state[3][3], self.state[1][3] = self.state[1][3], self.state[0][3], \
                                                                                 self.state[4][3], self.state[3][3]

    def up(self):
        self.state[0][0], self.state[0][2], self.state[0][7], self.state[0][5] = self.state[0][5], self.state[0][0], \
                                                                                 self.state[0][2], self.state[0][7]
        self.state[0][1], self.state[0][4], self.state[0][6], self.state[0][3] = self.state[0][3], self.state[0][1], \
                                                                                 self.state[0][4], self.state[0][6]
        self.state[5][2], self.state[1][2], self.state[2][2], self.state[4][2] = self.state[1][2], self.state[2][2], \
                                                                                 self.state[4][2], self.state[5][2]
        self.state[5][0], self.state[1][0], self.state[2][0], self.state[4][0] = self.state[1][0], self.state[2][0], \
                                                                                 self.state[4][0], self.state[5][0]
        self.state[5][1], self.state[1][1], self.state[2][1], self.state[4][1] = self.state[1][1], self.state[2][1], \
                                                                                 self.state[4][1], self.state[5][1]


    def down(self):
        self.state[3][0], self.state[3][2], self.state[3][7], self.state[3][5] = self.state[3][5], self.state[3][0], \
                                                                                 self.state[3][2], self.state[3][7]
        self.state[3][1], self.state[3][4], self.state[3][6], self.state[3][3] = self.state[3][3], self.state[3][1], \
                                                                                 self.state[3][4], self.state[3][6]
        self.state[5][2], self.state[1][2], self.state[2][2], self.state[4][2] = self.state[1][2], self.state[2][2], \
                                                                                 self.state[4][2], self.state[5][2]
        self.state[5][0], self.state[1][0], self.state[2][0], self.state[4][0] = self.state[1][0], self.state[2][0], \
                                                                                 self.state[4][0], self.state[5][0]
        self.state[5][1], self.state[1][1], self.state[2][1], self.state[4][1] = self.state[1][1], self.state[2][1], \
                                                                                 self.state[4][1], self.state[5][1]

    def front(self):
        self.state[1][0], self.state[1][2], self.state[1][7], self.state[1][5] = self.state[1][5], self.state[1][0], \
                                                                                 self.state[1][2], self.state[1][7]
        self.state[1][1], self.state[1][4], self.state[1][6], self.state[1][3] = self.state[1][3], self.state[1][1], \
                                                                                 self.state[1][4], self.state[1][6]

    def back(self):
        self.state[4][0], self.state[4][2], self.state[4][7], self.state[4][5] = self.state[4][5], self.state[4][0], \
                                                                                 self.state[4][2], self.state[4][7]
        self.state[4][1], self.state[4][4], self.state[4][6], self.state[4][3] = self.state[4][3], self.state[4][1], \
                                                                                 self.state[4][4], self.state[4][6]
