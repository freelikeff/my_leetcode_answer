#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/5/1 15:54 
# @Author : freelikeff 
# @Site : https://leetcode-cn.com/problems/longest-consecutive-sequence/description/
# @File : 128answer.py 
# @Software: PyCharm


# 先排序，然后动态规划，需要注意的就是会有重复元素，所以当有重复元素的时候，curr是保持不动的
# 时间复杂度nlogn,也就是排序的复杂度，空间复杂度常数，就两个临时变量
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        ans = 1
        curr = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                curr += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                ans = max(ans, curr)
                curr = 1

        return max(ans, curr)


# 这个是别人答案的改编版。先集合化去重，然后对于集合中的每一个元素，如果比它大一的数存在，呢么这个数我们不考虑
# 也就是说我们只考虑连续序列的终点数值，然后一直往下减到初始值，做统计即可
# 别人的方法是只考虑初始值，然后一直加至终点数值
class Solution2(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        ans = 1
        simple = set(nums)
        for num in simple:
            if num + 1 not in simple:
                curr = 0
                while num in simple:
                    curr += 1
                    num -= 1
                ans = max(ans, curr)
        return ans


if __name__ == "__main__":
    s = Solution2()
    inpt = [0, -1]
    answer = s.longestConsecutive(inpt)
    print(answer)
