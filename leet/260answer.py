#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/4/25 19:16 
# @Author : freelikeff 
# @Site : 
# @File : 260answer.py 
# @Software: PyCharm


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = 0
        for item in nums:
            temp ^= item
        n = len(bin(temp)) - 3  # 这个n表示移位次数
        a, b = 0, 0
        for i in nums:
            if i >> n & 1:  # 确定区分位是1还是0（与1求与相当于看最后移位是不是1）
                a ^= i
            else:
                b ^= i
        return a, b


if __name__ == "__main__":
    s = Solution()
    inpt = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
    answer = s.singleNumber(inpt)
    print(answer)
