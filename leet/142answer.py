#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 16:53
# @Author  : frelikeff
# @Site    : 
# @File    : 142answer.py
# @Software: PyCharm
from utils.makelinklist import ListNode


# 先判断有环否，有环的话在找入口
# 记录下环的长度length
# 前后指针再扫一遍，让前指针先走length步，然后前后速率一致向前直至重合到入口节点
class Solution2:
    def hasCycle(self, head: ListNode) -> ListNode or None:

        fast = head
        slow = head
        flag = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                flag = True
                break
        if not flag:
            return
        fast = fast.next
        length = 1
        while not (fast is slow):
            fast = fast.next
            length += 1
        fast = slow = head
        for i in range(length):
            fast = fast.next
        while not (fast is slow):
            fast = fast.next
            slow = slow.next
        return fast


# 别人的
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow

        return None
