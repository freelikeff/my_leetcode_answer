#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/8 12:04
# @Author  : frelikeff
# @Site    : 
# @File    : 109convert_sorted_list_to_binary_search_tree.py
# @Software: PyCharm
from utils.makelinklist import ListNode
from utils.maketree import TreeNode
from typing import List


# 给定一个排序的列表，生成平衡二叉搜索树
def list2BBST(nums: List) -> TreeNode:
    length = len(nums)
    if not length:
        return None
    if length == 1:
        return TreeNode(nums[0])
    if length == 2:
        root = TreeNode(nums[0])
        root.right = TreeNode(nums[1])
        return root
    if length == 3:
        root = TreeNode(nums[1])
        root.left = TreeNode(nums[0])
        root.right = TreeNode(nums[2])
        return root
    root_index = length // 2
    root = TreeNode(nums[root_index])
    root.left = list2BBST(nums[:root_index])
    root.right = list2BBST(nums[root_index + 1:])
    return root


# 调用排序数组生成平衡二叉树，也可用快慢指针找链表中间，此处略
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return list2BBST(values)


if __name__ == '__main__':
    from utils.makelinklist import makelinklist

    my_link = makelinklist([-10, -3, 0, 5, 9])
    s = Solution()
    answer = s.sortedListToBST(my_link)
    print(answer)
