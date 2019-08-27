#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 8:40
# @Author  : frelikeff
# @Site    : 
# @File    : 1170.py
# @Software: PyCharm
from typing import List


def f(s):
    ll = sorted(s)
    return ll.count(ll[0])


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        cous = [0] * 11
        qf = [f(item) for item in queries]
        wf = [f(item) for item in words]
        for item in wf:
            cous[item] += 1
        for i in range(1, 11):
            cous[i] += cous[i - 1]
        for i in range(1, 11):
            cous[i] = len(words) - cous[i]

        return [cous[item] for item in qf]


if __name__ == '__main__':
    s = Solution()
    queries = ["bbb", "cc"]
    words = ["a", "aa", "aaa", "aaaa"]
    ans = s.numSmallerByFrequency(queries, words)
    print(ans)
