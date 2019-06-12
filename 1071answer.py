#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/8 20:45
# @Author  : frelikeff
# @Site    : 
# @File    : 1071answer.py
# @Software: PyCharm


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        start = length1 = len(str1)
        length2 = len(str2)
        if not length1 or not length2:
            return ""
        if length1 <= length2:
            if length1 == 1:
                return str1 if set(str2) == {str1} else ""
            values = []

            for i in range(length1, 0, -1):
                if not length1 % i and not length2 % i:
                    values.append(i)
            for item in values:
                T = str1[:item]
                flag = True
                for i in range(1, length1 // item):
                    if str1[i * item:(i + 1) * item] != T:
                        flag = False
                        break

                if flag:
                    for i in range(length2 // item):

                        if str2[i * item:(i + 1) * item] != T:
                            flag = False
                            break

                if flag:
                    return T

            return ""
        if length1 > length2:
            if length2 == 1:
                return str2 if set(str1) == {str2} else ""
            values = []
            for i in range(length2, 0, -1):
                if not length1 % i and not length2 % i:
                    values.append(i)

            for item in values:
                T = str2[:item]
                flag = True
                for i in range(1, length2 // item):
                    if str2[i * item:(i + 1) * item] != T:
                        flag = False
                        break

                if flag:
                    for i in range( length1 // item):
                        if str1[i * item:(i + 1) * item] != T:
                            flag = False
                            break

                if flag:
                    return T

            return ""

# Solution().gcdOfStrings("LEET", "CODE")
print(Solution().gcdOfStrings("LEET", "CODE"))
