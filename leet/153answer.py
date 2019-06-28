#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 20:01
# @Author  : freelikeff
# @Site    : 
# @File    : 153answer.py
# @Software: PyCharm


# 找到突降点即可，如果没有突降点，那么说明有序，返回第一个元素
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[i]
        return nums[0]


# 递归，如果mid>两边界，说明small在[mid+1:],ruguo mid<两边界，说明small在[:mid+1],如果first<mid<end,那么说明顺序没乱
class Solution2(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 4:
            return min(nums)
        else:
            if nums[0] < nums[length // 2] < nums[-1]:
                return nums[0]
            elif nums[0] < nums[length // 2]:
                return self.findMin(nums[length // 2:])
            else:
                return self.findMin(nums[:length // 2 + 1])


if __name__ == "__main__":
    s = Solution2()
    inpt = [4, 5, 1, 2, 3]
    answer = s.findMin(inpt)
    print(answer)
