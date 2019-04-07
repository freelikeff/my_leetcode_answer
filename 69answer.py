#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 20:43
# @Author  : freelikeff
# @Site    : 
# @File    : 69answer.py
# @Software: PyCharm


# 其实应该用二分法来做，但是这里太小了我写不下了
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(x ** 0.5)


# memory over
class Solution1(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 4:
            return 1
        for ans in range(x):
            x_pre = ans ** 2
            if x_pre == x:
                return ans
            elif x_pre > x:
                return ans - 1


# time over
class Solution2(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 4:
            return 0 if x == 0 else 1
        x_pre = 1
        ans = 0
        while x_pre < x:
            ans += 1
            x_pre += (2 * ans + 1)

        return ans + 1 if x_pre == x else ans


if __name__ == "__main__":
    s = Solution2()
    inpt = 1745536076
    ans = s.mySqrt(inpt)
    print(ans)
