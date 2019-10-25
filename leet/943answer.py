#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 20:56
# @Author  : frelikeff
# @Site    : 
# @File    : 943answer.py # TODO
# @Software: PyCharm
from pprint import pprint
from typing import List
from itertools import permutations


def strrepeat(x, y):
    for ans in range(min(len(x), len(y)), -1, -1):
        if x.endswith(y[:ans]):
            return ans


# 暴利求解，直接超时。。。
class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        length = len(A)
        nums = [[0] * length for _ in range(length)]
        for i in range(length):
            for j in range(length):
                if i != j:
                    nums[i][j] = strrepeat(A[i], A[j])

        cover = -1
        for item in permutations(range(length), length):
            covers = 0
            for i in range(length - 1):
                covers += nums[item[i]][item[i + 1]]

            if covers > cover:
                ans = item
                cover = covers

        start = A[ans[0]]
        temp = ans[0]
        for rank in ans[1:]:
            start += A[rank][nums[temp][rank]:]
            temp = rank
        print(ans,)
        return start


if __name__ == '__main__':
    s = Solution()
    inpt = ["txvteggrtmylrxxknwub","lipgamrjnsfcqizch","teggrtmylrxxknwubv","uogduurswxthftx","akwnbruogduursw","uurswxthftxvteg","mylrxxknwubvlipga","ggrtmylrxxknwubvl","gzeindakwnbruogdu","thftxvteggrtmylrx"]
    print(s.shortestSuperstring(inpt))
    # gcta agt tca tgcatc
    # gcta agt tca tgcatc
