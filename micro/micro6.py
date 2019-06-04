#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 10:14
# @Author  : frelikeff
# @Site    : 
# @File    : micro6.py
# @Software: PyCharm
from typing import List


# lrd即为后序遍历，left,right,d
class Solution:
    def is_lrd(self, inpt: List) -> bool:
        # 如果长度是0,1,2那么肯定没问题
        if len(inpt) < 3:
            return True
        # 根节点是最后一个元素
        root = inpt[-1]
        # 设置遍历指针和左右子树标记位，因为如果标记位在遍历中没有赋值，说明根节点没有右子树，所以初始值应为最后一个位置
        i = 0
        flag = len(inpt) - 1  # 表示右子树的开始坐标
        while i < len(inpt) - 1:
            if inpt[i] > root:
                flag = i     # 找到左右分割点，即第一个大于根节点的树
                break
            i += 1

        while i < len(inpt) - 1:
            if inpt[i] < root:   # 如果在右子树中发现比根节点小的，直接返回False
                return False
            i += 1

        return self.is_lrd(inpt[:flag]) and self.is_lrd(inpt[flag:-1])  # 对左右子树递归判断


if __name__ == '__main__':
    s = Solution()
    inpt = [0, 0, 0, 0, 0, 0, 0]
    print(s.is_lrd(inpt))
