#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/31 20:42
# @Author  : freelikeff
# @Site    : 
# @File    : 36answer.py
# @Software: PyCharm



#自己的方法，由于开始对数独做了修改，所以不是很合理，但是由于值都是大于9且不重复，所以影响并不大
#分三次遍历
#首先将每行转换成集合，看长度是否等于9
#然后将每列转换成集合，看长度是否等于9，应用了集合推导式
#然后对每块化为集合，应用了解包操作*
class Solution:
    def isValidSudoku(self, board) -> bool:
        rank=10
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    board[i][j]=rank
                    rank+=1
        for item in board:
            if len(set(item))!=9:
                return False

        for j in range(9):
            if len({board[i][j] for i in range(9)}) != 9:
                return False

        for i in range(3):
            for j in range(3):
                if len({*board[3*i][3*j:3*j+3],*board[3*i+1][3*j:3*j+3],*board[3*i+2][3*j:3*j+3]}) != 9:
                    return False

        return True

#用了一个大集合，里面是元组，分别代表第几行存在某个值，某个值存在于某个列，以及某个块存在某个值，存在则返回F，不存在则添加
#                                     (i, b) in s      or (b, j) in s          or (i // 3, j // 3, b)
class Solution2:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        s = set()
        for i in range(9):
            for j in range(9):
                b = board[i][j]
                if b != '.':
                    continue
                if (i, b) in s or (b, j) in s or (i // 3, j // 3, b) in s:
                    return False
                s.add((i, b))
                s.add((b, j))
                s.add((i // 3, j // 3, b))
        return True


if __name__ == "__main__":
    s=Solution()
    inpt=[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    ans=s.isValidSudoku(inpt)
    print(ans)

