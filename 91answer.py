#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 16:51
# @Author  : freelikeff
# @Site    : 
# @File    : 91answer.py
# @Software: PyCharm


# 这个题改了一万年，边界条件多的一笔，这谁顶得住
class Solution:
    def numDecodings(self, s: str) -> int:

        # 一些边界条件
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        if s.find("00") >= 0:
            return 0
        my_record = [1 for i in range(len(s))]

        # 设置前两格
        if s[1] == "0":
            if int(s[0]) > 2:
                return 0
        elif int(s[:2]) < 27:
            my_record[1] = 2

        # 从第三个开始动态规划
        for i in range(2, len(s)):
            if s[i] == "0":
                if int(s[i - 1]) > 2:
                    return 0
                else:
                    my_record[i] = my_record[i - 2]

            elif s[i - 1] == "0":
                my_record[i] = my_record[i - 1]

            elif int(s[i - 1:i + 1]) < 27:
                my_record[i] = my_record[i - 1] + my_record[i - 2]

            else:
                my_record[i] = my_record[i - 1]

        print(my_record)
        return my_record[-1]


if __name__ == '__main__':
    s = Solution()
    inpt = "10245723"
    answer = s.numDecodings(inpt)
    print(answer)
