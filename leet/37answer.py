#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/24 8:38
# @Author  : frelikeff
# @Site    : 
# @File    : 37answer.py
# @Software: PyCharm
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        cols = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        pieces = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        blacks = []
        for i, h in enumerate(board):
            for j, item in enumerate(h):
                if item != ".":
                    rows[i].add(item)
                    cols[j].add(item)
                    pieces[(i // 3) * 3 + j // 3].add(item)
                else:
                    blacks.append((i, j))

        def helper(board):
            # 终止条件
            if not blacks:
                return True
            i, j = blacks.pop()
            for select in list("123456789"):
                if select not in rows[i] and select not in cols[j] and select not in pieces[(i // 3) * 3 + j // 3]:
                    board[i][j] = select
                    rows[i].add(select)
                    cols[j].add(select)
                    pieces[(i // 3) * 3 + j // 3].add(select)

                    if helper(board):
                        return True
                    else:
                        rows[i].remove(select)
                        cols[j].remove(select)
                        pieces[(i // 3) * 3 + j // 3].remove(select)

            blacks.append((i, j))
            return False

        helper(board)


if __name__ == '__main__':
    s = Solution()
    from pprint import pprint

    inpt = [list(".2.4....."),
            list("..9..7..1"),
            list("..1...73."),
            list(".5..1...2"),
            list("...9.6..."),
            list("1...3..4."),
            list(".94...3.."),
            list("7..6..5.."),
            list(".....3.2."),

            ]
    # pprint(inpt)
    s.solveSudoku(inpt)
    pprint(inpt)
