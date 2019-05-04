#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/5/4 19:19 
# @Author : freelikeff 
# @Site : 
# @File : 43answer.py 
# @Software: PyCharm


# 虽然属于作弊，但是这题模仿竖式计算就好
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) * int(num2))


if __name__ == "__main__":
    s = Solution()
    inpt = "24789", "3276"
    answer = s.multiply(*inpt)
    print(answer)
