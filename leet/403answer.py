#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 16:08
# @Author  : frelikeff
# @Site    : 
# @File    : 403answer.py
# @Software: PyCharm

from typing import List


def helper(nums, frontstep):
    if len(nums) == 1:
        return True
    if len(nums) == 2:
        return abs(nums[1] - nums[0] - frontstep) < 2

    if nums[0] + frontstep + 1 < nums[1]:
        return False
    if frontstep == 1:
        for step in (frontstep, frontstep + 1):
            position = nums[0] + step
            i = 1
            while nums[i] <= position:
                if nums[i] == position:
                    if helper(nums[i:], step):
                        return True
                    else:
                        break
                else:
                    i += 1



    else:

        for step in (frontstep - 1, frontstep, frontstep + 1):
            position = nums[0] + step
            i = 1
            while nums[i] <= position:
                if nums[i] == position:
                    if helper(nums[i:], step):
                        return True
                    else:
                        break
                else:
                    i += 1

    return False


# 多好的递归，结果又超时了
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        return helper(stones[1:], 1)


# 那还是用类似于BFS来做吧
# 还是超时了-_-
# 加了ns后就速度大幅提升，为什么？ TODO
class Solution2:
    def canCross(self, nums: List[int]) -> bool:
        if nums[1] != 1:
            return False
        deque = [(1, 1)]  # idx,frontstep
        end = len(nums) - 1
        ns=set()
        while deque:
            idx, frontstep = deque.pop(0)
            if nums[idx]+frontstep in ns:
                continue
            ns.add(nums[idx]+frontstep)
            if frontstep == 1:
                for step in (frontstep, frontstep + 1):
                    newposition = nums[idx] + step
                    i = idx + 1
                    while i <= end and nums[i] <= newposition:
                        if nums[i] == newposition:
                            if i == end:
                                return True
                            deque.append((i, step))
                            break
                        i += 1

            else:

                for step in (frontstep - 1, frontstep, frontstep + 1):
                    newposition = nums[idx] + step
                    i = idx + 1
                    while i <= end and nums[i] <= newposition:
                        if nums[i] == newposition:
                            if i == end:
                                return True
                            deque.append((i, step))
                            break
                        i += 1
            print(deque)
        return False


class Solution3(object):

    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[1] != 1:
            return False
        end = stones[-1]
        stones = set(stones)
        ns = set()
        # 第1位为当前位置 ， 第2位为上一位跳跃距离
        ol = [(1, 1)]
        while ol:
            i, k = ol.pop()
            if i == end:
                return True
            s = i + k
            if s in ns:
                continue
            ns.add(s)
            # ni下一步跳到的位置，nk跳到ni的跳跃距离
            for nk in (k - 1, k, k + 1):
                ni = i + nk
                if ni > i and ni in stones:
                    ol.append((ni, nk))
        return False


if __name__ == '__main__':
    s = Solution2()
    inpt = [0, 1, 3, 5, 6, 8, 12, 17]
    inpt2 = [0, 1, 2, 3, 4, 8, 9, 11]
    inpt3 = [0, 1, 3, 6, 10, 13, 15, 18]
    print(s.canCross(inpt3))
