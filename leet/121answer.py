#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/5/5 15:51 
# @Author : freelikeff 
# @Site : 
# @File : 121answer.py 
# @Software: PyCharm


# 动态规划，ans[i]记录的是第i天卖出的收益，所以最后返回的是max(ans),而不是ans[-1]
# 用一个常量空间记录之前的最低价，那么第i天之前的最低价为min（price[i-1],lower_price），ans[i]=当天价-最低价
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        ans = [0 for i in range(len(prices))]
        lower_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i - 1] < lower_price:
                lower_price = prices[i - 1]
            ans[i] =  prices[i]-lower_price
        print(ans)
        return max(ans)


if __name__ == '__main__':
    s = Solution()
    inpt = [7, 6, 4, 3, 1]
    answer = s.maxProfit(inpt)
    print(answer)
