#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 20:34
# @Author  : freelikeff
# @Site    : 
# @File    : 67answer.py
# @Software: PyCharm

# nothing to say,dajia douhui
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    s = Solution()
    inpt = "1010", "1011"
    ans = s.addBinary(*inpt)
    print(ans)
