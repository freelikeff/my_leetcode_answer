#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/5/5 10:42 
# @Author : freelikeff 
# @Site : 
# @File : 122answer.py 
# @Software: PyCharm


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        money = 0
        for i in range(1, len(prices)):
            money += max(0, prices[i] - prices[i - 1])
        return money


if __name__ == '__main__':
    s = Solution()
    inpt = [1, 7, 2, 3, 6, 7, 6, 7]
    answer = s.maxProfit(inpt)
    print(answer)
