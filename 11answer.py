#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/5/4 19:41 
# @Author : freelikeff 
# @Site : 
# @File : 11answer.py 
# @Software: PyCharm


# 我的暴力解法，time over
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        from itertools import combinations
        ans = 0
        for front, back in combinations(range(len(height)), 2):
            area = (back - front) * min(height[front], height[back])
            if area > ans:
                ans = area
        return ans


# 双指针法。开始时两个指针分别在两边，每次将矮的那个边往里移（因为S=H*W，H为矮边高度，如果移动高的边，呢么H不会变高，相反W必定减小）
class Solution2(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        areamax = 0
        while i < j:
            if height[i] >= height[j]:
                area_temp = height[j] * (j - i)
                j -= 1
            else:
                area_temp = height[i] * (j - i)
                i += 1
            if area_temp > areamax:
                areamax = area_temp
        return areamax


if __name__ == "__main__":
    s = Solution2()
    inpt = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    answer = s.maxArea(inpt)
    print(answer)
