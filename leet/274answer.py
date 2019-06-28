#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/4/25 12:26 
# @Author : freelikeff 
# @Site : 
# @File : 274answer.py 
# @Software: PyCharm


# 这道题能把我绕到姥姥家去
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        citations.sort(reverse=True)
        ans = 0
        for i in range(len(citations)):
            ans = max(ans, (min(i + 1, citations[i])))
        return ans


# pythonic
class Solution2(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))


if __name__ == "__main__":
    s = Solution()
    inpt = [4, 4, 0, 0]
    answer = s.hIndex(inpt)
    print(answer)
