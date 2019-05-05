#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/5/5 9:23 
# @Author : freelikeff 
# @Site : 
# @File : 72answer.py 
# @Software: PyCharm


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        height, width = len(word1), len(word2)
        if height == 0:
            return width
        elif width == 0:
            return height

        ans = [[0] * width for _ in range(height)]
        if word1[0] != word2[0]:
            ans[0][0] = 1

        # 先处理上边界
        for w in range(1, width):
            if word2[w] == word1[0]:
                ans[0][w] = w
            else:
                ans[0][w] = ans[0][w - 1] + 1

        # 再处理左边界
        for h in range(1, height):
            if word2[0] == word1[h]:
                ans[h][0] = h
            else:
                ans[h][0] = ans[h - 1][0] + 1

        # 开始规划：如果word1
        for h in range(1, height):
            for w in range(1, width):
                if word1[h] == word2[w]:
                    ans[h][w] = ans[h - 1][w - 1]
                else:
                    ans[h][w] = min(ans[h - 1][w - 1], ans[h - 1][w], ans[h][w - 1]) + 1
        return ans[-1][-1]


if __name__ == '__main__':
    s = Solution()
    inpt = "ros","horse"
    answer = s.minDistance(*inpt)
    print(answer)
