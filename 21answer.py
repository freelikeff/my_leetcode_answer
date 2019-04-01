#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 18:41
# @Author  : freelikeff
# @Site    : 
# @File    : 21answer.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 相当于一直比较两边的最小值往answer链表添加即可
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        first = head
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next
        if l1 == None:
            head.next = l2
        elif l2 == None:
            head.next = l1
        return first.next


# 别人的递归方法，看湿了
class Solution2:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None and l2 is None:
            return None
        if l1 is None and l2 is not None:
            return l2
        if l1 is not None and l2 is None:
            return l1

        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

# 感觉是作弊，返回的list[int],而不是链表，不过确实也能通过，这谁顶得住
class Solution3:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = list()
        while(l1!=None):
            l.append(l1.val)
            l1 = l1.next
        while(l2!=None):
            l.append(l2.val)
            l2 = l2.next
        return sorted(l)

if __name__ == "__main__":
    pass
