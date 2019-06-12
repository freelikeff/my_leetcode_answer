#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 10:58
# @Author  : frelikeff
# @Site    : 79 answer
# @File    : 12.py
# @Software: PyCharm
from typing import List


# 这里加上一点难度，打印出路径
def exist(matrix: List[List[str]], word: str) -> List[tuple]:
    height, width = len(matrix), len(matrix[0])
    assert word and height

    def dfs(h, w, index, flag):  # h,w代表进入的坐标，index代表字符串的第几个字符，flag代表以路过的字符

        if -1 < h < height and -1 < w < width and (h, w) not in flag:
            if matrix[h][w] != word[index]:
                return None
            if index == len(word) - 1:
                return [(h, w)]
            temp_top = dfs(h - 1, w, index + 1, flag + [(h, w)])
            if temp_top:
                return [(h, w)] + temp_top
            temp_down = dfs(h + 1, w, index + 1, flag + [(h, w)])
            if temp_down:
                return [(h, w)] + temp_down
            temp_left = dfs(h, w - 1, index + 1, flag + [(h, w)])
            if temp_left:
                return [(h, w)] + temp_left
            temp_right = dfs(h, w + 1, index + 1, flag + [(h, w)])
            if temp_right:
                return [(h, w)] + temp_right
        else:
            return None

    for i in range(height):
        for j in range(width):
            if matrix[i][j] == word[0]:
                return dfs(i, j, 0, [])


if __name__ == '__main__':
    matrix = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ASADFBCCEESE"
    print(exist(matrix, word))
