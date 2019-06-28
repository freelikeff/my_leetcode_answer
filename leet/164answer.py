#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 9:16
# @Author  : freelikeff
# @Site    : 
# @File    : 164answer.py
# @Software: PyCharm


# 一个编程语言没有排序函数是可怕的，有了排序函数却不去用，非要自己造轮子是可耻的。这道题除了排序也没什么其他点了，真香！
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 2:
            return 0
        nums.sort()
        if len(nums) == 2:
            return nums[1] - nums[0]

        max = nums[1] - nums[0]
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] > max:
                max = nums[i] - nums[i - 1]
        return max


if __name__ == "__main__":
    s = Solution()
    inpt = [1, 2, 1, 3, 5, 6, 4]
    ans = s.maximumGap(inpt)
    print(ans)