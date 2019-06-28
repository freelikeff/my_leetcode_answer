#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/4/28 10:02 
# @Author : freelikeff 
# @Site : 
# @File : 213answer.py 
# @Software: PyCharm


# 既然是个圈，那就分两种情况，带第0家和不带第0家.分别动态规划
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        elif len(nums) <= 3:
            return max(nums)

        # 带第0家,那么最后一家则不能偷
        ans = [nums[0], max(nums[0], nums[1]), max(nums[0] + nums[2], nums[1])]
        for i in range(3, len(nums) - 1):
            ans[0] = ans[1]
            ans[1] = ans[2]
            ans[2] = max(ans[0] + nums[i], ans[1])
        money = ans[-1]
        print(money)
        # 不带第0家，带最后一家
        ans = [nums[1], max(nums[1], nums[2]), max(nums[1] + nums[3], nums[2])]
        print(ans)
        for i in range(4, len(nums)):
            ans[0] = ans[1]
            ans[1] = ans[2]
            ans[2] = max(ans[0] + nums[i], ans[1])
            print(ans)
        print(ans[-1])
        return max(ans[-1], money)


if __name__ == "__main__":
    s = Solution()
    inpt = [1, 7, 9, 2]
    ans = s.rob(inpt)
    print(ans)
