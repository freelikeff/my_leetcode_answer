#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/5/2 19:32 
# @Author : freelikeff 
# @Site : 
# @File : 239answer.py 
# @Software: PyCharm


class MaxDeque(object):# TODO

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        self.save_max = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.values.append(x)
        if self.save_min:
            if x <= self.save_min[-1]:
                self.save_min.append(x)
        else:
            self.save_min.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.t.pop() == self.save_min[-1]:
            self.save_min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.t[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.save_min[-1]


# class Solution(object):
#     def maxSlidingWindow(self, nums, k):  #
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """


if __name__ == "__main__":
    # s = Solution()
    inpt = [1, 3, -1, -3, 5, 3, 6, 7]
    # ans = [1, 3, 3, 3, 5, 5, 6, 7, 7, 7]
    # answer = s.maxSlidingWindow(*inpt)
    # print(answer)
    my = MaxDeque()
    print(my.t)
    for item in inpt:
        my.push(item)
        print(my.getmax())
