#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 16:41
# @Author  : freelikeff
# @Site    : 
# @File    : 229answer.py
# @Software: PyCharm


# 基于collection模块的咱就不提了，没排面！（其实真香！）
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 3:
            return nums[:2]
        cur1, count1, cur2, count2 = nums[0], 0, 0.1, 0
        for item in nums:
            if item == cur1:
                count1 += 1
            elif item == cur2:
                count2 += 1
            elif count1 == 0:
                cur1, count1 = item, 1
            elif count2 == 0:
                cur2, count2 = item, 1
            else:
                count1 -= 1
                count2 -= 1
            print(cur1, count1, cur2, count2)
        ans = []
        if nums.count(cur1) > len(nums) // 3:
            ans.append(cur1)
        if nums.count(cur2) > len(nums) // 3:
            ans.append(cur2)
        return ans


if __name__ == "__main__":
    s = Solution()
    inpt = [1, 1, 1, 3, 3, 2, 2, 2]
    answer = s.majorityElement(inpt)
    print(answer)
