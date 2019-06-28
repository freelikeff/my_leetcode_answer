#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/7 21:44
# @Author  : frelikeff
# @Site    : 
# @File    : 191number_of_1_bits.py
# @Software: PyCharm

class Solution:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=0
        while n:
            n=n&(n-1)
            i+=1
        return i

if __name__ == '__main__':
    s=Solution()
    inpt=16
    print(s.hammingWeight(inpt))