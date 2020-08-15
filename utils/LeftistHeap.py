#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 15:05
# @Author  : frelikeff
# @Site    : 
# @File    : LeftistHeap.py
# @Software: PyCharm
"""
左偏树
解决普通的二叉堆无法合并的问题
"""


class LeftistNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.father = None
        self.dis = 0

    @property
    def isleave(self):
        return not self.left and not self.right

    def swap_lr_dis(self):
        if not self.left:
            self.left,self.right=self.right,self.left
            self.dis=0
            return

        if not self.right:
            self.dis = 0
            return

        if self.left.dis<self.right.dis:
            self.left, self.right = self.right, self.left
            self.dis=self.right.dis+1

# 最小左偏树
class LeftistTree:
    def __init__(self, init=None):
        if init is not None:
            self.root = LeftistNode(init[0])
            for item in init[1:]:
                self.push(item)
        else:
            self.root = LeftistNode(None)
        return

    def push(self, item):
        if self.root.val is None:
            self.root.val = item
            return

        self.merge(LeftistNode(item))

    def pop(self):

        ans = self.root.val
        if self.root.isleave:
            self.root.val = None
            return ans
        if self.root.left:
            self.root, node2 = self.root.left, self.root.right
            self.root.father = node2.father = None
            if node2:
                self.merge(node2)
        return ans

    def getTop(self):
        return self.root.val

    # 这样合并会将另一个树直接挂上来，所以需要删除掉第二棵树
    # 传进来的可以是树，那么需要将其变成根节点，也可以直接传入一个节点
    def merge(self, other):
        if not isinstance(other, LeftistNode):
            other = other.root
        assert isinstance(other, LeftistNode)
        self.root = LeftistTree._mergenode(self.root, other)

    @staticmethod
    def _mergenode(node1, node2):
        assert node1
        if not node2:
            return node1
        # 如果这个节点大于另一个节点值，那么需要交换
        if node1.val > node2.val:
            # 如果有父节点
            if node1.father:
                node1.father.right = node2
                node2.father = node1.father
                node1.father = None
                if node2.father.left.dis < node2.dis:
                    node2.fahter.left, node2.father.right = node2.father.right, node2.father.left

                LeftistTree._mergenode(node2, node1)
                node2.father.swap_lr_dis()
                return node2

            # 没有父节点，意味着是个根节点
            else:
                return LeftistTree._mergenode(node2, node1)

        # 这个节点小于等于另一个节点
        else:
            # 如果存在右节点，那么将右节点和另一个节点做merge
            if node1.right:
                ans= LeftistTree._mergenode(node1.right, node2)
                node1.

            # 如果没有右节点
            else:
                node2.father = node1
                # 如果也没有左节点或者左节点的距离小于另一个节点的距离，那么需要插入后左右交换
                if not node1.left or node1.left.dis < node2.dis:
                    node1.left, node1.right = node2, node1.left

                else:
                    node1.right = node2

                # 修改可能会涉及到的距离
                if not node1.right:
                    node1.dis = 0
                else:
                    node1.dis = node1.right.dis
                return node1
    # 调整一个节点左右距离的大小关系，以及修改自己的dis

    def __bool__(self):
        return self.root.val is not None


def showtree(root):
    def findh(root):
        if not root:
            return 0
        else:
            return max(findh(root.left), findh(root.right)) + 1

    def sstr(node):

        ans = str(node.val)

        length = len(ans)
        if length < 6:
            f = (6 - length) >> 1
            e = 6 - f
            return " " * f + ans + " " * e
        return ans

    h = findh(root)
    floor = [root]
    for i in range(1, h + 1):
        next_floor = []
        print(" " * 5 * (2 ** (h - i) - 1), end="")
        for item in floor:
            if item:
                next_floor.append(item.left)
                next_floor.append(item.right)
                print(" " + sstr(item) + " ", end="")
            else:
                next_floor.append(None)
                next_floor.append(None)
                print(" " * 10, end="")

            print(" " * 10 * (2 ** (h - i) - 1), end="")
        print("")
        floor = next_floor


if __name__ == '__main__':
    vals = [17, 66, 59, 7, 46, 28, 47, 90, 32, 49, 2, 63, 11, 99, 51]
    tree1 = LeftistTree([17, 66, 59, 7, 46, 28, 47, 90, 32, 49, 2, 63, 11, 99, 51])
    # for val in vals:
    #     tree1.push(vals)

    # tree2 = LeftistTree([13, 17, 12, 1, 9, 46])
    #
    # while tree1:
    #     print(tree1.pop())
