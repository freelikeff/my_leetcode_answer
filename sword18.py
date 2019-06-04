#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 19:00
# @Author  : frelikeff
# @Site    : 
# @File    : sword18.py
# @Software: PyCharm

from utils.maketree import TreeNode


# 这个函数是判断t是否是s子结构，leetcode572判断是不是子树，两个概念

def hasSubtree(s, t):
    flag = False
    if s and t:
        if s.val == t.val:
            flag = is_prefixtree(s.left, t.left) and is_prefixtree(s.right, t.right)
        if not flag:
            return hasSubtree(s.left, t) or hasSubtree(s.right, t)

    return flag


def is_prefixtree(s, t):
    if not t:
        return True
    if not s:
        return False
    if s.val == t.val:
        return is_prefixtree(s.left, t.left) and is_prefixtree(s.right, t.right)
    return False


if __name__ == '__main__':
    from utils.maketree import maketree_complex as maketree

    t = maketree([8, 9, 3], [9, 8, 3])
    s = maketree([8, 8, 9, 2, 4, 7, 7], [9, 8, 4, 2, 7, 8, 7])
    a, b = t.left, t.right
    c, d = s.left.left, s.left.right
    ans = hasSubtree(s, t)
    print(ans)
    print(is_prefixtree(c, a), is_prefixtree(d, b))
