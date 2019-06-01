#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 10:12
# @Author  : freelikeff
# @Site    : 
# @File    : 66answer.py
# @Software: PyCharm


# I don't think I can understand my code, even though a line of code looks cool.
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # this_num=int("".join([str(item) for item in digits]))     # 先将每个元素转换成字符，然后将字符链接成字符串，然后转换成数字
        # ans_num=this_num+1
        # ans_str=str(ans_num)
        # ans=list(ans_str)
        # return [int(item) for item in ans]

        return [int(item) for item in list(str(int("".join([str(item) for item in digits])) + 1))]


# not in-place
class Solution2:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)):

            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
        return [1] + [0] * len(digits)


if __name__ == "__main__":
    s = Solution()
    inpt = [1, 2, 3]
    ans = s.plusOne(inpt)
    print(inpt)
