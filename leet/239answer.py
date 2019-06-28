#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/5/2 19:32 
# @Author : freelikeff 
# @Site : 
# @File : 239answer.py 
# @Software: PyCharm


# 设计一个可以常数时间获得最大值的队列，自己尝试了很久，发现有点难
# 那就利用①最大栈155②利用两个最大栈实现一个队列232

class MaxDeque:
    def __init__(self):
        self.values = []
        self.save_max = []

    def push(self, x):
        self.values.append(x)
        if not self.save_max or x <= self.save_max[-1]:
            self.save_max.append(x)
        else:
            while self.save_max and self.save_max[-1] < x:
                self.save_max.pop()
            self.save_max.append(x)

    def pop(self):
        a = self.values.pop(0)
        if a == self.save_max[0]:
            self.save_max.pop(0)
        return a

    def getmax(self):
        return self.save_max[0]


class Solution(object):
    def maxSlidingWindow(self, nums, k):  #
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k==1 :
            return nums
        if len(nums)==k:
            return [max(nums)]
        ans=[]
        my_queue=MaxDeque()
        for i in range(k):
            my_queue.push(nums[i])
        ans.append(my_queue.getmax())

        for i in range(k,len(nums)):
            my_queue.push(nums[i])
            my_queue.pop()
            ans.append(my_queue.getmax())
        return ans

if __name__ == "__main__":
    s = Solution()
    inpt = [1, 3, -1, -3, 5, 3, 6, 7], 3
    # ans = [3, 3, 5, 5, 6, 7, 7, 7]
    answer = s.maxSlidingWindow(*inpt)
    print(answer)
    # s=MaxStack()
    # print(s.save_value, s.save_max)
    # s.push(1)
    # print(s.save_value, s.save_max)
    # s.push(3)
    # print(s.save_value, s.save_max)
    # s.push(-1)
    # print(s.save_value,s.save_max)
