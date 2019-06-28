#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 9:00
# @Author  : freelikeff
# @Site    : 
# @File    : 56answer.py
# @Software: PyCharm


def jiahe(interval1,interval2):
    return Interval(interval1.start, max(interval1.end, interval2.end))

# 多加了一个自己定义的函数，但是一起可以直接修改类，嘿嘿，加一个__add__即可
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]

        """
        mylist=sorted(intervals,key = lambda _: _.start)
        ans=[]
        for i in range(len(mylist)):
            if ans:
                if mylist[i].start>ans[-1].end:
                    ans.append(mylist[i])
                else:
                    ans.append(jiahe(ans.pop(),mylist[i]))
            else:
                ans.append(mylist[i])

        return ans


# 思路和我基本一样，但是代码更加优雅
class Solution2:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]

        """
        ans = []
        for item in sorted(intervals, key = lambda _: _.start):
            if ans and item.start <= ans [-1].end:
                ans[-1].end = max(item.end, ans [-1].end)
            else:
                ans.append(item)
        return ans
if __name__=="__main__":
    # Definition for an interval
    class Interval:
        def __init__(self, s=0, e=0):
                self.start = s
                self.end = e

    s=Solution2()
    inpt=[Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]
    ans = s.merge(inpt)
    for item in ans:
        print(item.start,item.end)