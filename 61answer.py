#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 20:00
# @Author  : freelikeff
# @Site    : 
# @File    : 61answer.py
# @Software: PyCharm


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# time over,但是我脚着还行
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        tran_list = []
        while head:
            tran_list.append(head.val)
            head = head.next
        length = len(tran_list)

        ans = [0 for i in range(length)]
        for i, item in enumerate(tran_list):
            ans[(i + k % length) % length] = item
            print(ans)
        start = None
        for i in range(length):
            this = ListNode(ans.pop())
            this.next = start
            start = this

        return start






if __name__ == "__main__":
    # Definition for singly-linked list.
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None


    s = Solution()
    a, b, c, d, e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    d.next = e
    c.next = d
    b.next = c
    a.next = b

    inpt = a, 5
    answer = s.rotateRight(*inpt)
    print(answer)
    while answer:
        print(answer.val)
        answer = answer.next
