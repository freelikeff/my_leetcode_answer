#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/7 20:44
# @Author  : frelikeff
# @Site    : 
# @File    : micro20.py
# @Software: PyCharm

def lc_substring(s: str, t: str) -> int:
    # 有一个是空字符串，那么直接返回0
    if not s or not t:
        return 0

    height, width = len(s), len(t)
    ans = [[0 for _ in range(width)] for _ in range(height)]
    # 初始化上边界
    for w in range(width):
        if t[w] == s[0]:
            ans[0][w] = 1
    # 初始化左边界
    for h in range(height):
        if t[0] == s[h]:
            ans[h][0] = 1
    # start dp
    for h in range(1, height):
        for w in range(1, width):
            if s[h] == t[w]:
                ans[h][w] = ans[h - 1][w - 1] + 1
    return max(max(row) for row in ans)

def lc_subsequence(s: str, t: str) -> int:
    # 有一个是空字符串，那么直接返回0
    if not s or not t:
        return 0

    height, width = len(s), len(t)
    ans = [[1 for _ in range(width)] for _ in range(height)]
    # 初始化上边界
    for w in range(width):
        if t[w] != s[0]:
            ans[0][w] = 0
        else:
            break
    # 初始化左边界
    for h in range(height):
        if t[0] != s[h]:
            ans[h][0] = 0
        else:
            break

    # start dp
    for h in range(1, height):
        for w in range(1, width):
            if s[h] == t[w]:
                ans[h][w] = ans[h - 1][w - 1] + 1
            else:
                ans[h][w] =max(ans[h][w - 1],ans[h - 1][w])

    return ans[-1][-1]


s="BDCABA"
t="ABCBDAB"
print(lc_subsequence(s,t))