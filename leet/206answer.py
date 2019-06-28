#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 9:20
# @Author  : frelikeff
# @Site    : 
# @File    : 206answer.py
# @Software: PyCharm

"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        else:
            new_head = self.reverseList(head.next)
            ans = self.reverseList(head.next)
            while new_head.next:
                new_head = new_head.next
            new_head.next = head
            return ans


# 迭代
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        front = None
        temp = head
        after = head.next
        while after:
            temp.next = front
            front = temp
            temp = after
            after = after.next
        temp.next = front
        return temp


# 上述算法的pythonic版本
class Solution3:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp, front = head, None
        while temp:
            front, front.next, temp = temp, front, temp.next
        return front
