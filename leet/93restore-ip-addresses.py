#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 11:29
# @Author  : frelikeff
# @Site    : 
# @File    : 93restore-ip-addresses.py
# @Software: PyCharm
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.helper(s, 4)[1]

    def helper(self, ss, n) -> (bool, List[str]):
        if n == 1:
            if int(ss) > 255 or (len(ss) > 1 and ss[0] == "0"):
                return False, None
            else:
                return True, [ss]

        ans = []
        for length in range(1, min(3, len(ss) - 1) + 1):
            if int(ss[:length]) > 255 or (length > 1 and ss[0] == "0"):
                continue
            tails = self.helper(ss[length:], n - 1)
            if tails[0]:
                for tail in tails[1]:
                    ans.append(ss[:length] + "." + tail)

        if len(ans):
            return True, ans
        return False, None


if __name__ == '__main__':
    s = Solution()
    inpt = "010010"
    print(s.restoreIpAddresses(inpt))
