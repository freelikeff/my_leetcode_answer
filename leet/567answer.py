#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/3 9:05
# @Author  : frelikeff
# @Site    : 
# @File    : 567answer.py
# @Software: PyCharm
from collections import Counter


def dict_is_same(dict1, dict2):
    for key in dict1:
        if dict1[key] != dict2[key]:
            return False
    return True


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if len(s1) == 1:
            return s2.find(s1) > -1

        cnt1 = Counter(s1)
        cnt2 = Counter(s2[:len(s1)])
        if dict_is_same(cnt1, cnt2):
            return True
        for i in range(len(s1), len(s2)):
            cnt2.update(s2[i])
            cnt2[s2[i - len(s1)]] -= 1
            if dict_is_same(cnt1, cnt2):
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    inpt = "abc", "mnfbcat"
    answer = s.checkInclusion(*inpt)
    print(answer)
