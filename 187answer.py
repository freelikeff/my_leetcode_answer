#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 14:42
# @Author  : freelikeff
# @Site    : 
# @File    : 187answer.py
# @Software: PyCharm


# 两个集合方便查找，也没什么点
class Solution:
    def findRepeatedDnaSequences(self, s: str):
        length = len(s)
        new_str = set()
        ans = set()
        for i in range(length - 9):
            cur = s[i:i + 10]
            if cur in new_str:
                ans.add(cur)
            else:
                new_str.add(cur)
        return list(ans)


if __name__ == "__main__":
    s = Solution()
    inpt = "AGCT"
    answer = s.findRepeatedDnaSequences(inpt)
    print(answer)
