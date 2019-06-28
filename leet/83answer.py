#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 16:29
# @Author  : frelikeff
# @Site    : 
# @File    : 83answer.py
# @Software: PyCharm
from utils.makelinklist import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        assert head
        start = head
        while start.next:
            if start.val == start.next.val:
                start.next = start.next.next
            else:
                start = start.next

        return head


# 递归
class Solution2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head and head.next:
            head.next = self.deleteDuplicates(head.next)
            return head.next if head.next.val == head.val else head
        return head