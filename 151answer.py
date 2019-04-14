#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 20:21
# @Author  : freelikeff
# @Site    : 
# @File    : 151answer.py
# @Software: PyCharm


class Solution:
    def reverseWords(self, s: str) -> str:
        this_list = s.split()
        return " ".join(this_list[::-1])


if __name__ == "__main__":
    s = Solution()
    inpt = "a good   example"
    answer = s.reverseWords(inpt)
    print(answer)
