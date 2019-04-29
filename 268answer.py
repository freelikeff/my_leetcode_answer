#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/4/25 12:59 
# @Author : freelikeff 
# @Site : 
# @File : 268answer.py 
# @Software: PyCharm


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        for i in range(n):
            ans ^= (i ^ nums[i])
        return ans ^ n


if __name__ == "__main__":
    s = Solution()
    inpt = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    answer = s.missingNumber(inpt)
    print(answer)
