#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 15:45
# @Author  : frelikeff
# @Site    : 
# @File    : maketree.py
# @Software: PyCharm
from typing import List
from pysnooper import snoop


class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


# 给定二叉树的前序遍历和中序遍历，获得该二叉树
def maketree(pre, tin):
    if len(pre) == 0 | len(tin) == 0:
        return None
    root = TreeNode(pre[0])
    root_index = tin.index(pre[0])
    root.left = maketree(pre[1:root_index + 1], tin[:root_index])
    root.right = maketree(pre[root_index + 1:], tin[root_index + 1:])
    return root


# 这个复杂是什么意思呢，主要是解决节点值有重复，上面的简单版会报错
def maketree_complex(pre, tin):
    if len(pre) == 0 | len(tin) == 0:
        return None
    root = TreeNode(pre[0])
    chosen_idex = []
    for i, item in enumerate(tin):
        if item == pre[0]:
            chosen_idex.append(i)
    for _ in chosen_idex:
        try:
            root.left = maketree(pre[1:_ + 1], tin[:_])
            root.right = maketree(pre[_ + 1:], tin[_ + 1:])
            return root
        except:
            continue


# DLR递归 参考leetcode144
def DLRdg(root: TreeNode) -> List[int]:
    if not root:
        return []
    else:
        return [root.val] + DLRdg(root.left) + DLRdg(root.right)


# DLR非递归
def DLRnodg(root: TreeNode) -> List[int]:
    ans = []
    stack = []
    if not root:
        return []

    stack.append(root)
    while stack:
        cur_node = stack.pop()
        if cur_node:
            ans.append(cur_node.val)
            stack.extend([cur_node.right, cur_node.left])
    return ans


# leetcode 94
def LDRdg(root: TreeNode) -> List[int]:
    if not root:
        return []
    else:
        return LDRdg(root.left) + [root.val] + LDRdg(root.right)


def LDRnodg(root: TreeNode) -> List[int]:
    if not root:
        return []
    # 初始化三连
    ans = []
    stack = []
    cur = root

    while cur or stack:  # y有一个不为空那就得继续迭代
        while cur:  # 顺着左边无脑进栈
            stack.append(cur)
            cur = cur.left
        if stack:  # 栈非空，就需要遍历了
            p = stack.pop()
            ans.append(p.val)
            cur = p.right
    return ans


def explore(node: TreeNode, res: list):
    if node:
        res.append(',' + str(node.val))
        res.append(',')
        explore(node.left, res)
        explore(node.right, res)
    else:
        res.append(',#')


# 层次遍历,用队列实现
def BT_level_order_traversal(root: TreeNode) -> List:
    if not root:
        return []
    ans = []
    deque = [root]
    while deque:
        temp_node = deque.pop(0)
        if temp_node:
            deque.append(temp_node.left)
            deque.append(temp_node.right)
            ans.append(temp_node.val)
        else:
            ans.append(None)
    return ans

# 后序遍历的偷懒方式，如果我没可以得到根右左，那么逆序即可得到左右根
# 根右左 可以利用前序遍历稍微修改一下即可。
def LRD_useDRL(root:TreeNode)-> List:
    ans = []
    stack = []
    if not root:
        return []

    stack.append(root)
    while stack:
        cur_node = stack.pop()
        if cur_node:
            ans.append(cur_node.val)
            stack.extend([cur_node.right, cur_node.left])
    return ans[::-1]


if __name__ == '__main__':
    preorder_seq = [4, 2, 1, 3, 6, 5, 7]
    middleorder_seq = [1, 2, 3, 4, 5, 6, 7]
    treeRoot1 = maketree_complex([8, 8, 9, 2, 4, 7, 7], [9, 8, 4, 2, 7, 8, 7])
    # my_tree = maketree([1, 2, 4, 5, 8, 9, 3, 6, 7], [4, 2, 8, 5, 9, 1, 6, 3, 7])
    print(DLRnodg(treeRoot1))
    print(LDRnodg(treeRoot1))
    an = []
    explore(treeRoot1, an)
    print(an)
