#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 20:27
# @Author  : freelikeff
# @Site    : 
# @File    : 77answer.py
# @Software: PyCharm


# 递归调用，我想要的答案
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n or k == 0:
            return []
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        if k == n:
            return [[i for i in range(1, n + 1)]]

        ans = self.combine(n - 1, k)
        for item in self.combine(n - 1, k - 1):
            item.append(n)
            ans.append(item)

        return ans


class Solution2(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        from itertools import combinations
        return list(combinations(range(1, n + 1), k))


if __name__ == "__main__":
    s = Solution2()
    inpt = 6, 3
    answer = s.combine(*inpt)
    print(answer)
