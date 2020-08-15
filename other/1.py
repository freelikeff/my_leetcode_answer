#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/15 15:35
# @Author  : frelikeff
# @Site    : 
# @File    : 1.py
# @Software: PyCharm
"""
题目详情：
给定一个字符编码格式，里面包含从a到y的25的小写字母，最大长度为4，编码格式如下：
a,aa,aaa,aaaa,aaab,aaac,...,aaay,aab,aaba,...,aayy,ab,aba,abaa,abab,...
ayyy,b,ba,baa,baaa,...
上述字符集分别按顺序对应编码0,1,2,...
给定一个字符集求编码/给定一个编码求字符集，二选一。
例如：输入baca，输出16331.
"""


def code2num(s: str)->int:
    fourthchange = 1
    thirdchange = 1 + 25 * fourthchange
    secondchange = 1 + 25 * thirdchange
    firstchange = 1 + 25 * secondchange
    changelist = [firstchange, secondchange, thirdchange, fourthchange]
    ans = 0
    for i, item in enumerate(s):
        ans += 1 + changelist[i] * (ord(item) - ord("a"))

    return ans - 1


# todo
def num2code(num:int)->str:
    return "None"

if __name__ == '__main__':
    print(code2num("baca"))
