#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/26 14:26
# @Author  : frelikeff
# @Site    : 
# @File    : 19answer.py
# @Software: PyCharm

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 感觉来个前后指针应该就可以
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        front, temp = head, head
        for i in range(n):
            front = front.next
        if not front:
            return temp.next
        while front.next:
            front = front.next
            temp = temp.next
        temp.next = temp.next.next
        return head
