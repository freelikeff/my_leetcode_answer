#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/4/28 10:40 
# @Author : freelikeff 
# @Site : 
# @File : 216answer.py 
# @Software: PyCharm

from itertools import combinations


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        for item in combinations(range(1, min(10, n)), k):
            if sum(item) == n:
                ans.append(item)
        return ans


if __name__ == "__main__":
    s = Solution()
    inpt = 3, 17
    ans = s.combinationSum3(*inpt)
    print(ans)
