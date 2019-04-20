#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 21:37
# @Author  : freelikeff
# @Site    : 
# @File    : 125answer.py
# @Software: PyCharm


class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_s = []
        for item in s:
            if item.isalpha():
                my_s.append(item.lower())
            elif item.isdigit():
                my_s.append(item)

        return my_s == my_s[::-1]


class Solution2:
    def isPalindrome(self, s: 'str') -> 'bool':
        s = s.lower()
        a = filter(str.isalnum, s)
        b = ''.join(list(a))
        if b == b[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    inpt = "A man, a plan, a canal: Panama"
    answer = s.isPalindrome(inpt)
    print(answer)
