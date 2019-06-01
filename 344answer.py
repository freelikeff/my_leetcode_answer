#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 10:37
# @Author  : frelikeff
# @Site    : 
# @File    : 344answer.py
# @Software: PyCharm

"""
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。



示例 1：

输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：

输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for i in range(length // 2):
            s[i], s[length - 1 - i] = s[length - 1 - i], s[i]


# 你大爷还是你大爷，库函数的性能就是高
class Solution2:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


if __name__ == '__main__':
    s = Solution()
    inpt = ["H", "a", "n", "n", "a", "h"]
    s.reverseString(inpt)
    print(inpt)
