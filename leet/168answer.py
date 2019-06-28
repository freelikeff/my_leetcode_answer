#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 14:10
# @Author  : freelikeff
# @Site    : 
# @File    : 168answer.py
# @Software: PyCharm


# 这个题最秀的是他从1开始，所以不能当成简单的26进制处理，得每次都减一
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        tran_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
        ans = []

        while n > 0:
            n -= 1
            ans.append(tran_list[n % 26])
            n //= 26
            # print(nn)
        return "".join(ans[::-1])


if __name__ == "__main__":
    s = Solution()
    inpt = 701
    answer = s.convertToTitle(inpt)
    print(answer)
