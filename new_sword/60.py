#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 21:38
# @Author  : frelikeff
# @Site    : 
# @File    : 60.py
# @Software: PyCharm

# 递归的算法是这样的，n次的和为s的概率，等于前n-1次的和为s-1且这次为1以及。。。
def probability_dg(n: int) -> dict:
    """

    :param n: 将骰子投掷n次
    :return: 返回一个字典，表示n次和以及概率
    """
    assert n
    if n == 1:
        return dict(zip(range(1, 6), [1 / 6] * 6))

    # 先把需要返回的字典建立起来，并初始化为0，将第一个以及最后一个直接算，后面就不算了
    ans = dict(zip(range(n, 6 * n + 1), [0] * (5 * n + 1)))
    ans[n] = ans[6 * n] = 1 / pow(6, n)

    # 由于只需要算一半，所以只需要算n至mid即可
    mid = (7 * n) // 2
    previous = probability_dg(n - 1)

    # 计算前半部分
    for s in range(n + 1, mid + 1):
        for num in range(1, 7):
            ans[s] += 1 / 6 * previous.get(s - num, 0)

    # 对称赋值后半部分
    for i in range(mid + 1, 6 * n):
        ans[i] = ans[7 * n - i]
    return ans


# 非递归的思路差不多，类比斐波那契，记忆一下上一个即可
def probability_ndg(n: int) -> dict:
    """

    :param n: 将骰子投掷n次
    :return: 返回一个字典，表示n次和以及概率
    """
    pass


if __name__ == '__main__':
    print(probability_dg(4))
