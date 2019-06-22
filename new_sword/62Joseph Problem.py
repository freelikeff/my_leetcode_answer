#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 10:22
# @Author  : frelikeff
# @Site    : 
# @File    : 62Joseph Problem.py
# @Software: PyCharm
from typing import List
from utils.makelinklist import makelinklist


# 环形链表类，为了这个题而定义的，所以编号0至n-1，val=编号，start表示返回的进入环的头结点编号
class CicleLink:
    def __init__(self, n, start):
        assert start < n
        head = temp = makelinklist([i for i in range(n)])
        for i in range(start):
            temp = temp.next
        self.head = temp
        while temp.next:
            temp = temp.next
        temp.next = head
        del head, temp


# 环形链表解决
class Solution:
    def JosephCircle(self, n: int, k: int, start: int = 0) -> List[int]:
        """
        n个人编号0至n-1围成一圈，从编号为start的人开始，每数到第k个人（这里从1开始数），就pop出这个人，求pop顺序
        """
        assert n
        if n == 1:
            return [0]
        my_cl = CicleLink(n, start)
        ans = []
        head = my_cl.head
        cou = 1
        while head.next != head:
            if cou == k:
                ans.append(head.val)
                head.val = head.next.val
                head.next = head.next.next
                cou = 1
            else:
                head = head.next
                cou += 1
        ans.append(head.val)
        return ans


# powerful math,参考剑指offer P303
class Solution2:
    def JosephCircle(self, n: int, k: int, start: int = 0) -> List[int]:
        """
        n个人编号0至n-1围成一圈，从编号为start的人开始，每数到第k个人（这里从1开始数），就pop出这个人，求pop顺序
        """
        assert n
        if n == 1:
            return [0]
        if not start:
            first = k % n - 1
            if first == -1:
                first = n - 1

            return [first] + [(item + first + 1) % n for item in self.JosephCircle(n - 1, k)]
        else:
            ans = self.JosephCircle(n, k)
            for i in range(len(ans)):
                ans[i] = (ans[i] + start) % n
            return ans


if __name__ == '__main__':
    s1 = Solution()
    s2 = Solution2()
    inpt = [100, 4,2]
    print(s1.JosephCircle(*inpt))
    print(s2.JosephCircle(*inpt))
