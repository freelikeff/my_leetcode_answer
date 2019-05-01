#!D:\coding\my_venv\Scripts\python3
# -*- coding: utf-8 -*- 
# @Time : 2019/5/1 22:41 
# @Author : freelikeff 
# @Site : 
# @File : 941answer.py 
# @Software: PyCharm


class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3 or A[0] >= A[1] or A[-1] >= A[-2]:
            return False

        flag = False
        for i in range(1, len(A) - 1):
            if A[i] == A[i + 1]:
                return False
            if flag:
                if A[i] > A[i + 1]:
                    continue
                else:
                    return False
            else:
                if A[i] < A[i + 1]:
                    continue
                else:
                    flag = True
        return flag


if __name__ == "__main__":
    s = Solution()
    inpt = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    answer = s.validMountainArray(inpt)
    print(answer)
