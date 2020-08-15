#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 8:38
# @Author  : frelikeff
# @Site    : 
# @File    : RedBlackTree.py
# @Software: PyCharm

# 默认颜色为红色


class RedBlackNode:
    def __init__(self, val, father=None, color=True):
        self.val = val
        self.left = self.right = None
        self.color = color
        self.father = father

    @property
    def isLeft(self):
        if self.father is None:
            raise ValueError("the node is a root")
        return self.father.left is self

    def getUncle(self):
        if self.father.isLeft:
            return self.father.father.right
        return self.father.father.left

    # 其实是伪后继节点，只在红黑树内用。
    # 没有进行有无后继节点验证，所以传入时需要保证有右节点
    def getAfter(self):
        start = self.right
        while start and start.left:
            start = start.left
        return start


class RedBlackTree:
    # 强制创建时必须有一个根节点
    def __init__(self):

        self.root = RedBlackNode(None)
        self.root.color = False

    def insert(self, newvalue):
        # 如果是个空树，直接给虚根节点赋值即可
        if self.root.val is None:
            self.root.val = newvalue
            return

        temp = self.root
        while temp:
            if newvalue == temp.val:
                return
            if newvalue > temp.val:
                if not temp.right:
                    temp.right = RedBlackNode(newvalue, temp)
                    temp = temp.right
                    break
                else:
                    temp = temp.right
            else:
                if not temp.left:
                    temp.left = RedBlackNode(newvalue, temp)
                    temp = temp.left
                    break
                else:
                    temp = temp.left

        while temp.father and temp.father.color:
            uncle = temp.getUncle()
            if not uncle or not uncle.color:  # 叔叔节点为None或者黑色
                if temp.isLeft:
                    rotate = RedBlackTree._rightrotate
                else:
                    rotate = RedBlackTree._leftrotate

                if temp.isLeft ^ temp.father.isLeft:  # 父子方向不同
                    memo = temp.father
                    rotate(self, memo)
                    temp = memo
                else:  # 父子方向相同
                    temp.father.color = False
                    temp = temp.father.father
                    temp.color = True
                    rotate(self, temp)
                    return
            else:  # 叔叔节点为红色
                temp.father.color = uncle.color = False
                uncle.father.color = True
                temp = uncle.father

        if not temp.father and temp.color:
            temp.color = False
            return

    def _leftrotate(self, node: RedBlackNode):
        if node is self.root:
            self.root = node.right

        elif node.isLeft:  # 说明要左旋的节点是一个左子树
            node.father.left = node.right
        else:
            node.father.right = node.right

        node.right.father = node.father
        node.father = node.right

        node.right = node.father.left
        node.father.left = node

        if node.right:
            node.right.father = node

    def _rightrotate(self, node: RedBlackNode):
        if node is self.root:
            self.root = node.left
        elif node.isLeft:  # 说明要左旋的节点是一个左子树
            node.father.left = node.left
        else:
            node.father.right = node.left

        node.left.father = node.father
        node.father = node.left

        node.left = node.father.right
        node.father.right = node

        if node.left:
            node.left.father = node

    def remove(self, val):
        # 如果只剩根节点
        if not self.root.left and not self.root.right:
            if val == self.root.val:
                self.root.val = None
            else:
                print("val not in tree")
            return

        temp = self.root
        while temp:
            if val < temp.val:
                if not temp.left:
                    print("val not in tree")
                    return
                temp = temp.left
            elif val > temp.val:
                if not temp.right:
                    print("val not in tree")
                    return
                temp = temp.right
            else:
                break

        # 如果是叶节点，用封装好的函数直接处理
        if not temp.left and not temp.right:
            self._removeleave(temp)
            self._sure_root_b()
            return

        # 左右子树都有，那么需要和后继节点交换,指针挪至后继节点
        # 那么就会变成单子树的情况
        if temp.left and temp.right:
            after = temp.getAfter()
            temp.val, after.val = after.val, temp.val
            temp = after

        if not temp.left and not temp.right:
            self._removeleave(temp)
            self._sure_root_b()
            return

        # 只有左子树或者只有右子树,此时只可能是T黑子红，那么直接子树替换掉T，并且将这个节点涂黑即可
        siglechild = bool(temp.left)
        self._remove_siglechild(temp, siglechild)
        self._sure_root_b()
        return

    # 删除黑叶子，兄弟同黑的情况
    def _removeTBlack(self, node, isleft=True):
        # 侄子如果存在的话必然是红叶子
        # 待删除节点是左黑叶子
        if isleft:
            brother = node.father.right
            nephew = brother.right
            if nephew:  # 存在则必然为红叶子
                # 父兄颜色互换，删除node，然后对父节点左旋,侄子变色
                brother.color, node.father.color = node.father.color, brother.color
                nephew.color = False
                node.father.left = None
                self._leftrotate(node.father)
                return
            elif brother.left:  # 存在则必然为红叶子
                nephew = brother.left
                nephew.color, brother.color = False, True
                self._rightrotate(brother)
                self._removeTBlack(node)
            else:  # 兄弟是一个黑叶子，没有侄子
                if node.father.color:  # 红色父亲带两个黑叶子
                    node.father.left = None
                    node.father.color, node.father.right.color = False, True
                else:  # 父子三人均黑
                    node.father.right.color = True
                    self._rightrotate(node.father)
                    self._remove_siglechild(node, siglechild=False, )
        # 待删除节点是右黑叶子
        else:
            brother = node.father.left
            nephew = brother.left
            if nephew:  # 存在则必然为红叶子
                # 父兄颜色互换，删除node，然后对父节点右旋
                brother.color, node.father.color = node.father.color, brother.color
                nephew.color = False
                node.father.right = None
                self._rightrotate(node.father)
                return
            elif brother.right:  # 存在则必然为红叶子
                nephew = brother.right
                nephew.color, brother.color = False, True
                self._leftrotate(brother)
                self._removeTBlack(node, False)
            else:  # 兄弟是一个黑叶子，没有侄子
                if node.father.color:  # 红色父亲带两个黑叶子
                    node.father.right = None
                    node.father.color, node.father.left.color = False, True
                else:  # 父子三人均黑
                    node.father.left.color = True
                    self._leftrotate(node.father)
                    self._remove_siglechild(node, siglechild=True)

    # 在删除黑叶子并且兄弟为红色的时候的第一步操作,父兄换色+旋转，转换至兄弟双黑
    def _changeFBcolor_rotate(self, node, isleft=True):
        if isleft:
            node.father.right.color = False
            node.father.color = True
            self._leftrotate(node.father)
        else:
            node.father.left.color = False
            node.father.color = True
            self._rightrotate(node.father)
        return

    # 删除有单子树的节点
    def _remove_siglechild(self, node, siglechild=True):  # True表示左
        if node is self.root:
            self.root = node.left if siglechild else node.right
            self.root.father = None
            return

        isleft = node.isLeft
        if siglechild:  # 代表只有左子树
            node.left.color = False
            if isleft:
                node.left.father, node.father.left = node.father, node.left
            else:
                node.left.father, node.father.right = node.father, node.left
            return

        else:  # 代表只有右子树
            node.right.color = False
            if isleft:
                node.right.father, node.father.left = node.father, node.right
            else:
                node.right.father, node.father.right = node.father, node.right
            return

    # 传入时确保是个叶子
    def _removeleave(self, node):
        if node.color:  # 如果是红叶子，(那必不可能是根节点)直接删除即可
            if node.isLeft:
                node.father.left = None
            else:
                node.father.right = None
            return

        # 黑叶子，情况就比较复杂了,首先兄弟必然存在。
        # 如果兄弟节点是红色，那么需要先转换至兄弟都是黑色的情况
        if node.isLeft and node.father.right.color:
            self._changeFBcolor_rotate(node)
            self._removeTBlack(node)
        elif not node.isLeft and node.father.left.color:
            self._changeFBcolor_rotate(node, False)
            self._removeTBlack(node, False)
        else:  # 兄弟双黑
            self._removeTBlack(node, node.isLeft)

        return

    def _sure_root_b(self):
        if not self.root.left and not self.root.right and self.root.color:
            self.root.color = False


def showtree(root: RedBlackNode):
    def findh(root: RedBlackNode):
        if not root:
            return 0
        else:
            return max(findh(root.left), findh(root.right)) + 1

    h = findh(root)
    floor = [root]

    def sstr(node):
        if node.color:
            ans = str(node.val) + "-r"
        else:
            ans = str(node.val) + "-b"

        length = len(ans)
        if length < 6:
            f = (6 - length) >> 1
            e = 6 - f
            return " " * f + ans + " " * e

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


def LdR_dg(root: RedBlackNode):
    if not root:
        return []
    return LdR_dg(root.left) + [root.val] + LdR_dg(root.right)


if __name__ == '__main__':
    from utils.TraverseTree import PreorderTraversal
    from random import shuffle

    tree = RedBlackTree()
    vals = [15, 63, 46, 47, 49, 28, 66, 99, 2, 11, 32, 51, 17, 90, 7, 59]

    for item in vals:
        tree.insert(item)

    prevals = [17, 66, 59, 7, 46, 28, 47, 90, 32, 49, 2, 63, 11, 99, 51]
    for item in prevals:
        tree.remove(item)
    showtree(tree.root)
    # print(LdR_dg(tree.root))
    # print(PreorderTraversal().DLR_ndg(tree.root))

    # shuffle(vals)
    vals = [99, 51, 15]

    for item in [15]:
        tree.remove(item)
        print("remove the val:", item)
        print(tree.root.val, tree.root.left, tree.root.right, tree.root.father)
