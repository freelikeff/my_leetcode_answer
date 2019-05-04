#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/5/4 19:06 
# @Author : freelikeff 
# @Site : 
# @File : 557answer.py 
# @Software: PyCharm

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([_[::-1] for _ in s.split()])


if __name__ == "__main__":
    s = Solution()
    inpt = "Let's take LeetCode contest"
    answer = s.reverseWords(inpt)
    print(answer)
