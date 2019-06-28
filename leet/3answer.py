#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/18 9:16
# @Author  : frelikeff
# @Site    : 
# @File    : 3answer.py
# @Software: PyCharm


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        assert s
        max_length = 1
        start = 0
        hashmap = dict()
        for i, item in enumerate(s):
            if hashmap.get(item, -1) >= start:
                if i - start > max_length:
                    max_length = i - start
                start, hashmap[item] = hashmap[item] + 1, i
            hashmap[item] = i

        return max(max_length,len(s)-start)


if __name__ == '__main__':
    s = Solution()
    inpt = "auq"
    answer = s.lengthOfLongestSubstring(inpt)
    print(answer)
