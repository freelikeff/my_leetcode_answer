#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time : 2019/5/5 16:14
# @Author : freelikeff
# @Site :  全排列
# @File : 46answer.py
# @Software: PyCharm


# 递归的写法.对于每个元素在开头的情况，都是其他元素的全排列
# 即将这些全排列分成length组，分别以每个元素开头，然后后面是其他元素的全排列
class Solution:
    def permute(self, nums):

        if len(nums) == 1:
            return [nums]

        n = len(nums)
        res = []

        for i in range(n):
            p = nums[:i] + nums[i + 1:]  # 临时的去掉第i个元素
            s = self.permute(p)
            for x in s:
                res.append([nums[i]] + x)

        return res


if __name__ == '__main__':
    import pprint
    s = Solution()
    inpt = list("01234")
    answer = s.permute(inpt)
    pprint.pprint(answer)



