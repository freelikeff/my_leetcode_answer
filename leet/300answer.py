#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 14:50
# @Author  : frelikeff
# @Site    : 
# @File    : 300answer.py
# @Software: PyCharm
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return length
        ans = [1] * length
        answer = 1
        for i in range(1, length):
            j = i - 1
            while j >= ans[i] - 1:
                if nums[j] < nums[i] and ans[j] + 1 > ans[i]:
                    ans[i] = ans[j] + 1
                j -= 1

            if ans[i] > answer:
                answer = ans[i]
        return answer


import bisect


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        ans = [nums[0]]  # 必定递增
        for number in nums[1:]:
            if ans and number > ans[-1]:
                ans.append(number)
            else:
                idx = bisect.bisect_left(ans, number)
                if number < ans[idx]:
                    ans[idx] = number
        return len(ans)


if __name__ == '__main__':
    s = Solution2()
    inpt = [10, 9, 2, 5, 3, 7, 101, 18]
    print(s.lengthOfLIS(inpt))
