#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 16:40
# @Author  : frelikeff
# @Site    : 
# @File    : 141answer.py
# @Software: PyCharm
from utils.makelinklist import ListNode
# 原题，快慢指针，返回bool即可
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False


# 需要返回环的入口节点,142answer
class Solution2:
    def hasCycle(self, head:ListNode):
        pass
