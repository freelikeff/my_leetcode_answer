#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 19:49
# @Author  : freelikeff
# @Site    : 
# @File    : 79answer.py
# @Software: PyCharm


# the first time i write DBF,so copy.but i understand it.
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        height, width = len(board), len(board[0])

        def dfs(a, b, index, flag):
            if a < 0 or b < 0 or a >= height or b >= width or board[a][b] != word[index] or (a, b) in flag:
                return False
            elif board[a][b] == word[index] and index == len(word) - 1:
                return True
            if dfs(a + 1, b, index + 1, flag + [(a, b)]):
                return True
            elif dfs(a - 1, b, index + 1, flag + [(a, b)]):
                return True
            elif dfs(a, b + 1, index + 1, flag + [(a, b)]):
                return True
            elif dfs(a, b - 1, index + 1, flag + [(a, b)]):
                return True
            else:
                return False

        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, []):
                        return True
        return False


if __name__ == "__main__":
    s = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    word = "ASFDECF"
    answer = s.exist(board, word)
    print(answer)
