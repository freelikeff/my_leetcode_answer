#!E:\pycharm\my_venv\Scripts\python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 20:01
# @Author  : freelikeff
# @Site    : 
# @File    : 88answer.py
# @Software: PyCharm

"""
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

"""


# 我这破代码，不看也罢
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ans = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
            print(ans)
        if i == m:
            for rank in range(j, n):
                ans.append(nums2[rank])
        else:
            for rank in range(i, m):
                ans.append(nums1[rank])
            print(ans)
        nums1[:] = ans


# 好看倒是好看,但是对于数组1后面有多余空间的话，对后面的0 也会进行排序，所以有漏洞
class Solution2:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n]=nums2[:]
        nums1.sort()


if __name__ == "__main__":
    s = Solution2()
    a, b, c, d = [1, 2, 3, 0, 0, 0,0,0], 3, [2, 5, 6], 3
    ans = s.merge(a, b, c, d)
    print(a)
