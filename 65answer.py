#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 10:42
# @Author  : freelikeff
# @Site    : 
# @File    : 65answer.py
# @Software: PyCharm


class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except:
            return False


if __name__ == '__main__':
    s = Solution()
    inpt = "0"
    answer = s.isNumber(inpt)
    print(answer)
