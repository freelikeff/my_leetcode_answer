#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 9:01
# @Author  : frelikeff
# @Site    : 
# @File    : 5164answer.py
# @Software: PyCharm
from utils.makelinklist import ListNode, makelinklist, showlink


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        if not head or (head.val == 0 and not head.next):
            return None
        start = head
        ans = []
        while head.next:
            value = head.val
            if not value:
                head = head.next
                continue
            if -value in ans:
                idx = ans.index(-value)
                ans = [item + value for item in ans[:idx]]
            else:
                ans = [item + value for item in ans]
                ans.append(value)
            head = head.next
        value = head.val

        # 处理最后一个节点
        if -value in ans:
            idx = ans.index(-value)
            ans = [item + value for item in ans[:idx]]
            if len(ans) > 1:
                for i in range(len(ans) - 1):
                    ans[i] -= ans[i + 1]

        else:
            if len(ans) > 1:
                for i in range(len(ans) - 1):
                    ans[i] -= ans[i + 1]
            if value:
                ans.append(value)

        print(ans)
        # 如果全部删除完了，那么返回None
        if not ans:
            return None

        # 如果还有剩余节点
        while start:
            if start.val != ans[0]:
                start = start.next
            else:
                break
        # 这说明就剩这一个节点了，且是最后一个
        if not start.next:
            return start

        # 保留一个最终返回的节点和前置节点
        ans_head = front = start
        start = start.next
        if len(ans) == 1:

            ans_head.next = None
            return ans_head

        ans.append(None)
        i = 1

        while start:
            if start.val == ans[i]:
                front = start
                start = start.next
                i += 1
            else:
                if start.next:
                    start.val = start.next.val
                    start.next = start.next.next
                else:
                    front.next = None
                    break

        return ans_head


if __name__ == '__main__':
    s = Solution()
    my_link = makelinklist([2, 0])
    answer = s.removeZeroSumSublists(my_link)

    showlink(answer)
