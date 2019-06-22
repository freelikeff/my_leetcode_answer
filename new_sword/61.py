#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 21:19
# @Author  : frelikeff
# @Site    : 
# @File    : 61.py
# @Software: PyCharm
from typing import List

hash_map = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
            "king": 0}


def is_straight(poker: List[str]) -> bool:
    """
    :param poker: 有五个元素的列表，代表拿到的五张牌，两张王可以是任意牌
    :return: 是否是顺子，是的话返回True
    """
    nums = [hash_map[item] for item in poker if item != "king"]
    kings = 5 - len(nums)
    nums.sort()
    for i in range(1, len(nums)):
        delt = nums[i] - nums[i - 1]
        if not delt:
            return False
        elif not delt - 1:
            continue
        else:
            kings -= delt - 1
            if kings < 0:
                return False
    return True


if __name__ == '__main__':
    poker = ["A", "4", "5", "king", "king"]
    print(is_straight(poker))
