#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/5/4 20:35 
# @Author : freelikeff 
# @Site : 
# @File : 15answer.py
# @Software: PyCharm


# 暴力求解，time over
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import combinations
        ans = set()
        for i, j, k in combinations(nums, 3):
            if i + k + j == 0:
                ans.add(tuple(sorted([i, j, k])))
        return list(ans)


class Solution2(object): # TODO
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        shunxu = sorted(nums)
        for i in range(len(shunxu)):
            if shunxu[i] > 0:
                continue






if __name__ == "__main__":
    s = Solution()
    inpt = [-1, 0, 1, 2, -1, -4]
    answer = s.threeSum(inpt)
    print(answer)
