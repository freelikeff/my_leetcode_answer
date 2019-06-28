#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 20:19
# @Author  : frelikeff
# @Site    : 
# @File    : 23answer.py
# @Software: PyCharm

"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""
from utils.makelinklist import ListNode
from typing import List
from functools import reduce


# 把所有节点加入列表，然后排序，其实是暴利解法，因为之前的有序信息没用上，但是时间就是快，这谁顶得住
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        dummy = pre = ListNode(-1)
        nums = []
        for node in lists:
            while node:
                nums.append(node)
                node = node.next
        for node in sorted(nums, key=lambda n: n.val):
            pre.next = node
            pre = pre.next

        return dummy.next


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = ListNode(0)
    first = head
    while l1 and l2:
        if l1.val > l2.val:
            head.next = l2
            l2 = l2.next
        else:
            head.next = l1
            l1 = l1.next
        head = head.next
    if not l1:
        head.next = l2
    elif not l2:
        head.next = l1
    return first.next


# 利用合并两个有序链表的函数，然后reduce
class Solution2:
    def mergeKLists(self, inpt: List[ListNode]) -> ListNode:
        if not len(inpt):
            return None
        return reduce(mergeTwoLists, inpt)


# 递归
class Solution3:
    def mergeKLists(self, inpt: List[ListNode]) -> ListNode:
        if not any(inpt):
            return None
        min_node = min(inpt, key=lambda item: item.val if item else 9223372036854775807)
        update_index = inpt.index(min_node)
        inpt[update_index] = inpt[update_index].next
        min_node.next = self.mergeKLists(inpt)
        return min_node
