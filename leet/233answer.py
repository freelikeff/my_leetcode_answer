#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/4/25 21:24 
# @Author : freelikeff 
# @Site : 
# @File : 233answer.py 
# @Software: PyCharm

class Solution:
    def countDigitOne(self, n: int) -> int:  # TODO
        count = 0
        for i in range(1, n + 1):
            count += (str(i).count("1"))
        return count


if __name__ == "__main__":
    s = Solution()
    inpt = 824883294
    answer = s.countDigitOne(inpt)
    print(answer)
