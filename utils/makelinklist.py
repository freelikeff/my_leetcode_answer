#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 15:44
# @Author  : frelikeff
# @Site    : 
# @File    : makelinklist.py
# @Software: PyCharm

# 给一个列表创建一个链表
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def makelinklist(order: List) -> ListNode or None:
    if not len(order):
        return None
    ans = ListNode(order[0])
    ans.next = makelinklist(order[1:])
    return ans


def showlink(start: ListNode):
    # step=start
    # while step:
    #     print(step.val,end="-->")
    #     step=step.next
    # print("None")

    while start:
        print(start.val, end="-->")
        start = start.next
    print("None")


if __name__ == '__main__':
    preorder_seq = [4, 2, 1, 3, 6, 5, 7]
    my_link = makelinklist(preorder_seq)
    showlink(my_link)
