#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 10:39
# @Author  : frelikeff
# @Site    : 
# @File    : 4answer_.py
# @Software: PyCharm

"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
"""


def find_k_min(nums1, nums2, k):  # 都不为空，且第一个短
    if k == 1:
        return min(nums1[0], nums2[0])
    if k == len(nums1) + len(nums2):
        return max(nums1[-1], nums2[-1])
    if k > len(nums1):
        if k > len(nums2):
            left, right = k - len(nums2), len(nums1) - 1  # 闭区间，左右边界都包括
            if nums1[-1] <= nums2[k - len(nums1)]:  # 排除右边界
                return max(nums1[-1], nums2[k - len(nums1) - 1])
            while 1:
                idx = (left + right) // 2
                if k - idx == len(nums2):
                    if nums1[idx] >= nums2[- 1]:
                        return max(nums1[idx - 1], nums2[- 1])
                    else:
                        left = idx + 1
                        continue

                elif nums1[idx - 1] <= nums2[k - idx] and nums1[idx] >= nums2[k - idx - 1]:
                    return max(nums1[idx - 1], nums2[k - idx - 1])
                elif nums1[idx - 1] > nums2[k - idx]:
                    right = idx - 1
                else:
                    left = idx + 1
        else:
            left, right = 1, len(nums1) - 1  # 闭区间，左右边界都包括
            if nums1[-1] <= nums2[k - len(nums1)]:  # 排除右边界
                return max(nums1[-1], nums2[k - len(nums1) - 1])
            if nums1[0] >= nums2[k - 1]:  # 排除左边界
                return nums2[k - 1]
            while 1:
                idx = (left + right) // 2
                if nums1[idx - 1] <= nums2[k - idx] and nums1[idx] >= nums2[k - idx - 1]:
                    return max(nums1[idx - 1], nums2[k - idx - 1])
                elif nums1[idx - 1] > nums2[k - idx]:
                    right = idx - 1
                else:
                    left = idx + 1

    else:  # k<=len(nums1)
        left, right = 1, k - 1  # 闭区间，左右边界都包括
        if nums1[k - 1] <= nums2[0]:  # 排除右边界
            return nums1[k - 1]
        if nums1[0] >= nums2[k - 1]:  # 排除左边界
            return nums2[k - 1]
        while 1:
            idx = (left + right) // 2
            if nums1[idx - 1] <= nums2[k - idx] and nums1[idx] >= nums2[k - idx - 1]:
                return max(nums1[idx - 1], nums2[k - idx - 1])
            elif nums1[idx - 1] > nums2[k - idx]:
                right = idx - 1
            else:
                left = idx + 1


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not len(nums1):
            if len(nums2) & 1:
                return nums2[len(nums2) // 2]
            else:
                return (nums2[len(nums2) // 2 - 1] + nums2[len(nums2) // 2]) / 2
        if not len(nums2):
            if len(nums1) & 1:
                return nums1[len(nums1) // 2]
            else:
                return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2

        index_left = (len(nums1) + len(nums2) + 1) // 2
        index_right = (len(nums1) + len(nums2) + 2) // 2
        print(find_k_min(nums1, nums2, index_left), find_k_min(nums1, nums2, index_right))
        if len(nums1) <= len(nums2):
            return (find_k_min(nums1, nums2, index_left) + find_k_min(nums1, nums2, index_right)) / 2
        if len(nums1) > len(nums2):
            return (find_k_min(nums2, nums1, index_left) + find_k_min(nums2, nums1, index_right)) / 2


if __name__ == "__main__":
    s = Solution()
    inpt = [3, 4], [1, 2]
    answer = s.findMedianSortedArrays(*inpt)
    print(answer)
