#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 10:04
# @Author  : freelikeff
# @Site    : 
# @File    : 169answer.py
# @Software: PyCharm


# 排序，然后用一个长度为n/2的窗口去卡，如果窗口两端点相同，这个窗口内必然是众数了
# 这样的消耗主要在排序上，时间复杂度nlogn,如果线性扫过去，则需记录统计结果，那么空间复杂度就会比较高
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        num_of_zhong = (len(nums) + 1) // 2 - 1
        print(num_of_zhong)
        for i in range(len(nums) // 2 + 1):
            if nums[i] == nums[i + num_of_zhong]:
                return nums[i]


# 我心态崩了呀兄弟，既然窗口长度不小于一半，那么中间值必然在窗口，这智商，以后就告别自行车了
class Solution2:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) // 2]


# 摩尔投票，消消乐,时间复杂度n,空间复杂度常量
class Solution3(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return nums[0]
        cur, count = nums[0], 0
        for item in nums:
            if item==cur:
                count+=1
            elif count==0:
                cur=item
                count = 1
            else:
                count-=1

        return cur


# 这就是我说的计数了
class Solution4:
    def majorityElement(self, nums):
        import collections
        cnts = collections.Counter(nums)

        for i, cnt in cnts.items():
            if cnt > len(nums) // 2:
                return i


# 这不是作弊吗，最骚的是时间还最快。那就只能委屈你放在第四个了。
class Solution5:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import random
        while True:
            r = random.choice(nums)
            if nums.count(r) > len(nums) / 2:
                return r


if __name__ == "__main__":
    s = Solution()
    inpt = [3, 3, 4]
    answer = s.majorityElement(inpt)
    print(answer)
