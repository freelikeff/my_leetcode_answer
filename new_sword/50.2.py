#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 22:25
# @Author  : frelikeff
# @Site    : 
# @File    : 50.2.py
# @Software: PyCharm

from typing import List


# 输入的应该是一个字符流（这里用一个最终版str代替）
# 需要返回的是一个动态的结果，即已有字符串中第一个只出现一次的字符
# 所以这里返回一个列表
def first_sigle_in_chr_stream(str) -> List:
    ans = []
    infinitely_max = 1 << 31
    hash_map = dict()
    for i, char in enumerate(str):
        if char not in hash_map:
            hash_map[char] = i
        else:
            hash_map[char] = infinitely_max
        ans.append(min(hash_map, key=hash_map.get))
    print(hash_map)
    return ans


if __name__ == '__main__':
    inpt = "googlekel"
    ans = first_sigle_in_chr_stream(inpt)
    print(ans)
