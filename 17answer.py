#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 18:19
# @Author  : freelikeff
# @Site    : 
# @File    : 17answer.py
# @Software: PyCharm

TRAN_DICT={'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

# 应该是一个动态规划的思想，比较简单，也pythonic
class Solution:
    def letterCombinations(self, digits: str):
        if digits == '':
            return []
        ans = ['']
        for num in digits:
            ans = [pre + suf for pre in ans for suf in TRAN_DICT[num]]
        return ans


if __name__ == "__main__":
    s=Solution()
    inpt="274"
    answer=s.letterCombinations(inpt)
    print(answer)
