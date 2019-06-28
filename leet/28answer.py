#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 9:01
# @Author  : freelikeff
# @Site    : 
# @File    : 28answer.py
# @Software: PyCharm

"""
KMP算法历史遗留问题 cite https://blog.csdn.net/v_july_v/article/details/7041827
"""

# 暴力循环解法，没什么可说的
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        length=len(needle)
        if length==len(haystack):
            if haystack==needle:
                return 0
            return -1
        for i in range(len(haystack)-length+1):
            if haystack[i:i+length] == needle:
                return i
        return -1


# 使用内置函数，pythonic
class Solution2:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        return haystack.index(needle)




if __name__ == "__main__":
    s=Solution2()
    inpt="aaaaa","bba"
    answer=s.strStr(*inpt)
    print(answer)
