#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 15:33
# @Author  : freelikeff
# @Site    : 
# @File    : KMP.py
# @Software: PyCharm


def next_list(s: str) -> list:
    ans = [-1 for _ in range(len(s))]
    i, k = 0, -1
    while i < len(s) - 1:
        if k == -1 or s[i] == s[k]:
            i += 1
            k += 1
            ans[i] = k
        else:
            k = ans[k]

    return ans


def kmp_match(big_s, small_s):
    len1, len2 = len(big_s), len(small_s)
    assert len1>len2, "the length of the main_str must longer than the pattern_str"
    the_next = next_list(small_s)
    i, j = 0, 0
    while i < len1:
        if j == -1 or big_s[i] == small_s[j]:
            i += 1
            j += 1
        else:
            j = the_next[j]
        if j == len2:
            return i - len2

    # 到这里就意味着没找到了
    return -1


if __name__ == "__main__":
    main_str = "abcabfffff"
    pattern_s = "abcdef"
    print(kmp_match(main_str,pattern_s))
