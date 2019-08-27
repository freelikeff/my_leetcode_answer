#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 8:37
# @Author  : frelikeff
# @Site    : 
# @File    : 1169.py
# @Software: PyCharm

from itertools import combinations


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        my_set = set()
        my_dict = {}
        for rank, item in enumerate(transactions):
            name, time, amount, city = item.split(",")
            if int(amount) > 1000:
                my_set.add(rank)
            if name in my_dict:
                my_dict[name].append([int(time), city, rank])
            else:
                my_dict[name] = [[int(time), city, rank]]

        for value in my_dict.values():
            if len(value) < 2:
                continue
            for one, other in combinations(value, 2):
                if abs(one[0] - other[0]) < 61 and one[1] != other[1]:
                    my_set.add(one[2])
                    my_set.add(other[2])

        return [transactions[i] for i in my_set]


if __name__ == '__main__':
    s = Solution()
    inpt = transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
    ans = s.invalidTransactions(inpt)
    print(ans)