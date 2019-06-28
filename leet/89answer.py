#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/5/5 8:53 
# @Author : freelikeff 
# @Site : 
# @File : 89answer.py 
# @Software: PyCharm


# 格雷编码， G(i) = i ^ (i>>2) ，第i个格雷数是i 与 i>>2 的异或
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [i ^ i >> 1 for i in range(1 << n)]


if __name__ == '__main__':
    def tran(num,n):
        er=bin(num)[2:]
        return "0"*(n-len(er))+er
    s = Solution()
    inpt = 4
    answer = s.grayCode(inpt)
    old=[_ for _ in range(1 << inpt)]
    print([tran(item,inpt) for item in answer])
    print([tran(item, inpt) for item in old])
