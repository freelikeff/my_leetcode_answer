#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 8:26
# @Author  : freelikeff
# @Site    : 
# @File    : 154answer.py
# @Software: PyCharm


# 其实就是想用二分，但其实直接min，也不慢
class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l < r and nums[l] >= nums[r]:
            mid = (l + r) // 2
            # print(l,r,mid)
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1

        return nums[l]


if __name__ == "__main__":
    s = Solution()
    inpt = [3, 3, 3, 4, 5, 0, 0, 1, 2]
    ans = s.findMin(inpt)
    print(ans)
