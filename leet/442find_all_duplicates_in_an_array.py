#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 18:38
# @Author  : frelikeff
# @Site    : 
# @File    : 442find_all_duplicates_in_an_array.py
# @Software: PyCharm
from typing import List


#
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        assert nums
        ans = []
        for item in nums:
            idx = abs(item) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
            else:
                ans.append(idx + 1)

        return ans


if __name__ == '__main__':
    s = Solution()
    inpt = [2, 3, 2, 3, 4, 1, 5, 5, 6]
    ans = s.findDuplicates(inpt)
    print(ans)
