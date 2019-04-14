#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 20:22
# @Author  : freelikeff
# @Site    : 
# @File    : 155answer.py
# @Software: PyCharm


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.save_value = []
        self.save_min = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.save_value.append(x)
        if self.save_min:
            if x <= self.save_min[-1]:
                self.save_min.append(x)
        else:
            self.save_min.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.save_value.pop() == self.save_min[-1]:
            self.save_min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.save_value[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.save_min[-1]


if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(3)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_3, param_4)
