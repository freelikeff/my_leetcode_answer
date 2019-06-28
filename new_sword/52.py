#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/23 19:01
# @Author  : frelikeff
# @Site    : 
# @File    : 52.py
# @Software: PyCharm
from utils.makelinklist import ListNode, makelinklist


# 返回两个链表的第一个公共节点
# 分别遍历，求出长度l1,l2,那么公共节点即可知
def firstPublicNode(s: ListNode, t: ListNode) -> ListNode or None:
    if not s or not t:
        return None
    s_length = t_length = 0
    ss = s
    tt = t
    while s.next:
        s = s.next
        s_length += 1
    while t.next:
        t = t.next
        t_length += 1

    if s_length > t_length:
        for _ in range(s_length - t_length):
            ss = ss.next
    else:
        for _ in range(t_length - s_length):
            tt = tt.next
    while ss != tt:
        ss = ss.next
        tt = tt.next
    return ss


if __name__ == '__main__':
    pub = makelinklist([3,4,5])
    f = first = makelinklist([9, 8, 7, 6, 5])
    s = second = makelinklist([11, 12,18,44,50,31])
    while s.next:
        s = s.next
    s.next = pub
    while f.next:
        f = f.next
    f.next = pub
    ans = firstPublicNode(first, second)
    print(ans.val)
