#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 11:53
# @Author  : frelikeff
# @Site    : 
# @File    : 42answer.py
# @Software: PyCharm
from typing import List


# 自己写的，稍显稚嫩
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        if len(height) == 3:
            return min(max(0, height[0] - height[1]), max(0, height[2] - height[1]))
        for i in range(len(height) - 1):
            if height[i] > height[i + 1]:
                start = i
                break
        else:
            return 0
        for i in range(len(height) - 1, start, -1):
            if height[i] > height[i - 1]:
                end = i
                break
        else:
            return 0

        memo = []
        summ = temp = 0
        for item in height[start:end + 1]:
            if not memo:  # 记录是空的
                if item:
                    memo.append(item)
            else:  # 记录不为空
                if item < memo[0]:
                    memo.append(item)
                    temp += (memo[0] - item)
                else:
                    summ += temp
                    temp = 0
                    memo = [item]

        if len(memo) == 1:
            return summ
        return summ + self.trap(memo[::-1])


# 别人的思路，相当于多一步预处理
# 这个辅助函数其实和上面差不多，但是由于传进来的数组最后一个数是最大值，所以保证必可以卡全，所以不用递归了
def helper(height):
    if len(height) < 3:
        return 0

    if len(height) == 3:
        return max(height[0] - height[1], 0)

    for i in range(len(height) - 1):
        if height[i] > height[i + 1]:
            start = i
            break

    else:
        return 0

    memo = []
    summ = temp = 0
    for item in height[start:]:
        if not memo:  # 记录是空的
            if item:
                memo.append(item)
        else:  # 记录不为空
            if item < memo[0]:
                memo.append(item)
                temp += (memo[0] - item)
            else:
                summ += temp
                temp = 0
                memo = [item]

    return summ


class Solution2:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        max_idx = height.index(max(height))
        if not max_idx:
            return helper(height[::-1])
        if max_idx == len(height) - 1:
            return helper(height)

        return helper(height[:max_idx + 1]) + helper(height[len(height) - 1:max_idx - 1:-1])


class Solution3:  #
    def trap(self, height: List[int]) -> int:
        ans = 0
        left = [0]
        right = [0]
        for item in height:
            left.append(max(left[-1], item))

        for item in reversed(height):
            right.append(max(right[-1], item))

        for i in range(1, len(height) - 1):
            ans += (min(left[i + 1], right[-i - 1]) - height[i])
        return ans


class Solution4:  # 神秘代码，花了一个小时看懂了，别问，第二遍估计又不懂了
    def trap(self, height: List[int]) -> int:
        ans = 0
        h1 = 0
        h2 = 0
        for i in range(len(height)):
            h1 = max(h1, height[i])
            h2 = max(h2, height[-i - 1])
            ans += h1 + h2
        return ans - sum(height) - len(height) * h1


if __name__ == '__main__':
    s = Solution3()
    inpt = [2, 0, 2]

    ans = s.trap(inpt)

    print(helper([2, 0, 2]))
