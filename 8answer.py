#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 9:37
# @Author  : freelikeff
# @Site    : 
# @File    : 8answer.py
# @Software: PyCharm


# 这个是比较传统的方法
class Solution:
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans, s = 0, s.strip()  # 去掉字符串前后的空格，这里没有改变原有字符串！strip函数，去除前后的空白字符（包括'\n', '\r',  '\t',  ' '）
        if len(s) == 0:
            return ans

        i, positive = 0, True
        if s[0] == '+' or s[0] == '-':
            i, positive = 1, s[i] == '+'

        while i < len(s):
            if not s[i].isdigit():
                break
            else:
                ans = ans * 10 + (ord(s[i]) - ord('0'))
            i += 1

        min_i32, max_i32 = -2 ** 31, 2 ** 31 - 1
        return min(ans, max_i32) if positive else max(min_i32, -ans)


# 正则表达式，比较高级的方法
class Solution2(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        import re  # 引入正则化模块

        # 正则化中^代表用^后面的开头，[-+]?表示[-+]可以出现，也可以不出现，\d匹配所有数字，\d+数字后面可以连接无数数字，但不能是其他东西，包括空格和字母
        list_s = re.findall(r"^[-+]?\d+", s.strip())  # 删除前，后空格。这样容易导致开始碰到字母就为空列表

        if not list_s:
            return 0  # 字母开始列表是空的,直接返回0
        else:
            num = int(''.join(list_s))  # 列表转化为字符串，然后转化为整数
            if num > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif num < -2 ** 31:
                return -2 ** 31
            else:
                return num


if __name__ == "__main__":
    s = Solution2()
    inpt = " wert987  978"
    answer = s.myAtoi(inpt)
    print(answer)
    print(inpt)
