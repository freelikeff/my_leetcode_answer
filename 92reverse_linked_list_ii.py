#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/7 19:48
# @Author  : frelikeff
# @Site    : 
# @File    : 92reverse_linked_list_ii.py
# @Software: PyCharm
from utils.makelinklist import ListNode, makelinklist, showlink


# 代码过于丑陋，就不加注释了，关键点在于分了两种情况，反转的部分是否从头结点开始
class Solution:
    # 反转第m节点到第n节点，头结点是第一个节点，
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if n == m:
            return head
        if m == 1:
            # 反转的部分不包括end，相当于全反转中的None
            front = None
            temp = sep = head
            after = head.next
            for i in range(n - 1):
                temp.next = front
                front = temp
                temp = after
                after = after.next
            temp.next = front
            sep.next = after
            return temp
        else:
            f_sep = head
            start = head.next
            for i in range(m - 2):
                f_sep = f_sep.next
                start = start.next
            front = None
            temp = e_sep = start
            after = start.next
            for i in range(n - m):
                temp.next = front
                front = temp
                temp = after
                after = after.next
            temp.next = front
            f_sep.next = temp
            e_sep.next = after
            return head


class Solution2:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dum = ListNode(0)
        dum.next = head
        pre = dum
        if m == n: return head
        for i in range(1, m):
            pre = pre.next
        head = pre.next
        for i in range(m, n):
            nex = head.next
            head.next = nex.next
            nex.next = pre.next
            pre.next = nex
        return dum.next


if __name__ == '__main__':
    my_link = makelinklist([1, 2, 3])
    s = Solution2()
    m, n = 2, 3
    answer = s.reverseBetween(my_link, m, n)
    showlink(answer)
