#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 9:29
# @Author  : frelikeff
# @Site    : 
# @File    : 5answer.py
# @Software: PyCharm

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""
#from pprint import pprint as print


# 动态规划，空间复杂度O(n^2)
# 递归方式 ans[i,j] = True  when i=j
#                  = True   when i+1=j  if s[i]=s[j]
#                  = True  when j-i>1  if  ans[i+1][j-1] and s[i]=s[j]
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = [[False] * len(s) for _ in range(len(s))]
        f, e = 0, 0
        # 对角初始置True
        for i in range(len(ans)):
            ans[i][i] = True
        for det in range(1, len(s)):
            for start in range(0, len(s) - det):
                if det == 1:
                    if s[start] == s[start + 1]:
                        ans[start][start + 1] = True
                        f, e = start, start + 1

                else:
                    if ans[start + 1][start + det - 1] and s[start] == s[start + det]:
                        ans[start][start + det] = True
                        f, e = start, start + det
        return s[f:e + 1]


# Manacher(马拉车)算法
class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 预处理
        s = "#" + "#".join(s) + "#"
        print(s)
        memo = [1] * len(s)
        pos, right = 0, 0
        for i in range(1, len(s) - 1):
            if i < right:
                memo[i] = min(memo[2 * pos - i], right - i)
            # 开始拓展
            while i - memo[i] >= 0 and i + memo[i] < len(s) and s[i - memo[i]] == s[i + memo[i]]:
                memo[i] += 1
            # 更新
            if i + memo[i] > right:
                right = i + memo[i] - 1
                pos = i
        max_loc = memo.index(max(memo))
        return s[max_loc - memo[max_loc]+1:max_loc + memo[max_loc]].replace("#", "")


if __name__ == "__main__":
    s = Solution2()
    inpt = "babad"
    answer = s.longestPalindrome(inpt)
    print(answer)
