#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/4/25 10:35 
# @Author : freelikeff 
# @Site : 
# @File : 278answer.py 
# @Software: PyCharm


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        mid = (l + r) // 2
        while l < r:
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
            mid = (l + r) // 2
        return mid


def isBadVersion(mid):
    if mid:
        pass
