#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 10:11
# @Author  : frelikeff
# @Site    : 
# @File    : 33.py
# @Software: PyCharm


from typing import List


def is_BST_LRD(seq: List) -> bool:
    if len(seq) < 3:
        return True
    root = seq[-1]
    idx = -1  # 意为右子树的开始，默认值
    for i in range(len(seq) - 1):
        if seq[i] > root:
            idx = i
            break  # 意味着左子树扫完
    if idx != -1:
        for i in range(idx + 1, len(seq) - 1):
            if seq[i] < root:
                return False

        return is_BST_LRD(seq[:idx]) and is_BST_LRD(seq[idx:-1])
    else:
        return is_BST_LRD(seq[:-1])


if __name__ == '__main__':
    inpt = [5, 12, 6, 9, 11, 10, 8]
    print(is_BST_LRD(inpt))