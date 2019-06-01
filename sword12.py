#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 16:05
# @Author  : frelikeff
# @Site    : 
# @File    : sword12.py
# @Software: PyCharm
from typing import List


# from itertools import product
# def print_one2maxndigit(n:int):
#     for item in product("0123456789",repeat=n):
#         print("".join(item))
#
#
# print_one2maxndigit(4)


def add1(inpt: List[str], length: int):
    flag = -1
    for i in range(length):
        if inpt[length - 1 - i] != "9":
            flag = length - 1 - i
            inpt[flag] = str(int(inpt[flag]) + 1)
            break
    for i in range(flag + 1, length):
        inpt[i] = "0"


def print_one2maxndigit(n: int):
    a = ["0" for _ in range(n)]
    while set(a) != {"9"}:
        print("".join(a))
        add1(a, n)
    print("".join(a))
    return


print_one2maxndigit(4)
