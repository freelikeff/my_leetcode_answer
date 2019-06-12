#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 19:38
# @Author  : frelikeff
# @Site    : 
# @File    : 8.py
# @Software: PyCharm


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def make_com_tree(pre, tin):
    if len(pre) == 0 | len(tin) == 0:
        return None
    root = TreeLinkNode(pre[0])
    root_index = tin.index(pre[0])
    part_left = make_com_tree(pre[1:root_index + 1], tin[:root_index])
    part_right = make_com_tree(pre[root_index + 1:], tin[root_index + 1:])
    if part_left:
        part_left.next = root
    if part_right:
        part_right.next = root
    root.right = part_right
    root.left = part_left
    return root


# 中序,前序，后序遍历的next
class Solution:  # TODO: LRD
    def LDR_GetNext(self, pNode):
        # write code here
        if pNode.right:  # 如果有右子树，那么返回右子树的最左边
            temp = pNode.right
            while temp.left:
                temp = temp.left
            return temp

        # 没有右子树，那就需要父节点信息
        if not pNode.next:  # 如果不存在父节点（此时的情况已经是没有右子树了），说明已经遍历完了
            return None

        if pNode == pNode.next.left:  # 此节点是父节点的左子树，那么说明父节点的左边遍历完了，则下一个就是父节点
            return pNode.next

        # 没有右子树，并且是父节点的右子树，那么久稍微有点麻烦，需要一直上溯，知道找到一个节点是父节点的左子节点
        temp = pNode.next
        while temp.next:
            if temp == temp.next.left:
                return temp.next
            temp = temp.next
        return None

    def DLR_GetNext(self, pNode):
        # write code here
        # 如果有左子树，那么返回左子节点
        if pNode.left:
            return pNode.left
        # 如果有右子树，那么返回右子节点
        if pNode.right:
            return pNode.left

        # 只剩下叶子节点情况了，需要父节点信息
        # 这个时候说明这个节点所在的这支树以及他的父节点都遍历完了
        # 呢么需要知道这个叶子是左还是右
        temp = pNode
        while temp.next:
            if temp is temp.next.left:
                if temp.next.right:
                    return temp.next.right
            temp = temp.next

        return


if __name__ == '__main__':
    my_tree = make_com_tree([1, 2, 4, 5, 8, 9, 3, 6, 7], [4, 2, 8, 5, 9, 1, 6, 3, 7])
    print(my_tree)
    inpt = my_tree.right.right
    print(inpt.val)
    s = Solution()
    ans = s.DLR_GetNext(inpt)
    print(ans.val)
