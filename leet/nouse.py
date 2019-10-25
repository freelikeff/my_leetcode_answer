#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 9:33
# @Author  : frelikeff
# @Site    : 
# @File    : nouse.py
# @Software: PyCharm
from typing import List

# def fenjie(n):
#     ans=[1]
#     while n!=1:
#         for i in range(2,n):
#             if n%i==0:
#                 ans.append(i)
#                 n//=i
#                 break
#         print(ans)
# print(fenjie(772235))

# t = int(input())
# for i in range(t):
#     n = int(input())
#     s = 0
#     for j in range(n):
#         x1, y1, x2, y2 = [int(item) for item in input().split()]
#         s += (abs(y1 - y2) + 1) * (abs(x1 - x2) + 1)
#     print(s)

# # n, k = [int(item) for item in input().split()]
# n,k=27579,28
# ans = 1
# for cheng in range(n, n - k, -1):
#     ans *= cheng
#     # if ans > 772235:
#     #     ans %= 772235
#
# print(ans%772235)

# def func(a):
#     """
#     :param a: List of 1,0
#     :param n: int ,表示1-n的排列,n=len(a)+1
#     :return: int
#     """
#     ans = [1]
#
#     for i, item in enumerate(a[::-1]):
#         if item:
#             ans.append(sum(ans))
#             for k in range(i, -1, -1):
#                 ans[k] = ans[k + 1] - ans[k]
#         else:
#             ans.insert(0, sum(ans))
#             for k in range(1, i + 2):
#                 ans[k] = ans[k - 1] - ans[k]
#
#     return sum(ans)
#
#
# def showit(a, n, memo, idx, base):
#     if idx == n - 1:
#         rest = sum(range(1, n + 1)) - sum(memo)
#         if a[idx - 1] ^ (rest > base):
#             return [[rest]]
#         else:
#             return None
#     ans = []
#     if not idx:
#         for select in range(1, n + 1):
#             temp = showit(a, n, memo + [select], idx + 1, select)
#             if temp:
#                 ans.extend([[select] + item for item in temp])
#
#     elif a[idx - 1] == 0:
#         for select in range(base + 1, n + 1):
#             if select in memo:
#                 continue
#             temp = showit(a, n, memo + [select], idx + 1, select)
#             if temp:
#                 ans.extend([[select] + item for item in temp])
#     else:
#         for select in range(1, base):
#             if select in memo:
#                 continue
#             temp = showit(a, n, memo + [select], idx + 1, select)
#             if temp:
#                 ans.extend([[select] + item for item in temp])
#
#     return ans if ans else None
#
#
# a = [1, 1, 0]
# answer = showit(a, len(a) + 1, [], 0, -1)
# print(func(a))
# print(answer)
# print(len(answer))
#
#
# def sign(x):
#     if x < 0:
#         return 0
#     else:
#         return 1
#
#
# for item in answer:
#     print([sign(item[i] - item[i + 1]) for i in range(len(a))])

# import random
#
#
# def func(m):
#     rest = set(range(2, m + 1))  # 起始点是1
#     start = 1
#     while 1:
#         temp = random.choice([-1, 1])
#         if start + temp == m + 1:
#             start = 1
#         elif start + temp == 0:
#             start = m
#         else:
#             start += temp
#         if start in rest:
#             if len(rest) == 2 :
#                 return start
#             else:
#                 rest.remove(start)
#
#
# m = 20
# cishu = 10000
# counter = list(range(m))
# for i in range(cishu):
#     counter[func(m) - 1] += 1
#
# for i in range(m):
#     counter[i] /= cishu
#
# print(counter[1:])

# def func(s):
#     assert s[0] == "r" and s[-1] == "l"
#     ans = [0] * len(s)
#     memo = [0]
#     start = "rl"
#     flag = 0
#     for i, char in enumerate(s):
#         if char != start[flag]:
#             memo.append(i)
#             flag = (flag + 1) % 2
#
#     memo.append(len(s))
#     print(memo)
#     flag = True
#     for i in range(len(memo) - 1):
#         length = memo[i + 1] - memo[i]
#         if flag:  # 一段r
#
#             ans[memo[i + 1] - 1] += (length + 1) >> 1
#             ans[memo[i + 1]] += length >> 1
#
#         else:  # 一段l
#             ans[memo[i]] += (length + 1) >> 1
#             ans[memo[i] - 1] += length >> 1
#
#         flag = not flag
#         print(ans)
#
#     return ans
#
#
# print(func("rrlrl"))


# def ff(n):
#     one, two, three, four = [1, 2, 3, 4]
#     five = four + two + one
#     for i in range(n - 5):
#         five, four, three, two, one = four + two + one, five, four, three, two
#
#     return five
#
# print(ff(100))

# import random
#
#
# def travel():
#     position = 0
#     steps = 1
#     position += random.choice((-1, 1))
#     while position:
#         steps += 1
#         position += random.choice((-1, 1))
#     return steps
#
#
# Ex = []
# for i in range(10):
#     summ = 0
#     for j in range(1000):
#         summ += travel()
#     Ex.append(summ / 1000)
#
# print(Ex)
#
# neibours = {(-1, -1, 2), (2, -1, -1), (-1, 2, -1)}
#
#
# def fun(nums: tuple):  # 输入为三国壮丁
#     memo = set()
#     node = tuple(sorted(nums))
#     deque = [node]
#     memo.add(node)
#     while deque:
#         a, b, c = deque.pop(0)
#         for da, db, dc in neibours:
#             na, nb, nc = a + da, b + db, c + dc
#             node = tuple(sorted([na, nb, nc]))
#             if 0 <= na and 0 <= nb and 0 <= nc and node not in memo:
#                 if node[0] == node[1] or node[1] == node[2]:
#                     return True
#                 memo.add(node)
#                 deque.append(node)
#
#     return False
#
#
# if __name__ == '__main__':
#     inpt = (0,1,8)
#
#     print(fun(inpt))


# def func(n: int, nPerson):  # len(nPerson)=n+1,idx=0无意义，只是为了idx=楼层
#     nMinFloor, TargetFloor = 0, 1
#     N1, N2, N3 = 0, nPerson[1], 0
#     for i in range(2, n + 1):
#         N3 += nPerson[i]
#         nMinFloor += nPerson[i] * (i - 1)
#
#     for i in range(2, n + 1):
#         if N1 + N2 < N3:
#             TargetFloor = i
#             nMinFloor += (N1 + N2 - N3)
#             N1 += N2
#             N2 += nPerson[i]
#             N3 -= nPerson[i]
#
#         else:
#             break
#
#     return TargetFloor
#
#
# print(func(10, [0, 0,1,2,3,4,5,6,7,8,9]))
# print(func(10, [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]))

# 二叉树层次遍历，感觉复杂度太高
# def func(n):
#     # 0,1,2分别表示操作为ACV
#     # 元素tuple表示 步数，操作后剪切板长度，以及操作后总长度
#     if n < 3:
#         return 0
#
#     deque = [([1], 3, 1, 2)]  # 1表示ac，0表示v
#     maxx = 2
#     maxoper = []
#     while deque:
#         oper, level, memol, length = deque.pop(0)
#         if level < n:
#             # if level >= n - 3:
#                 deque.append((oper + [1], level + 3, length, 2 * length))
#                 deque.append((oper + [0], level + 1, memol, length + memol))
#             # else:
#             #     if length >= 3 * memol:
#             #         deque.append((oper + [1], level + 3, length, 2 * length))
#         elif level == n:
#             if length > maxx:
#                 maxx = length
#                 maxoper = oper
#         else:
#             if memol > maxx:
#                 maxx = memol
#                 maxoper = oper
#                 maxoper.pop()
#     return maxx, maxoper
#
#
# for i in range(3, 30):
#     print(func(i))

# (3, [1, 0])
# (4, [1, 0, 0])
# (5, [1, 0, 0, 0])
# (6, [1, 1, 0])
# (9, [1, 0, 1, 0])
# (12, [1, 0, 1, 0, 0])
# (16, [1, 0, 0, 1, 0, 0])
# (20, [1, 0, 0, 1, 0, 0, 0])
# (27, [1, 0, 1, 0, 1, 0])
# (36, [1, 0, 1, 0, 1, 0, 0])
# (48, [1, 0, 1, 0, 0, 1, 0, 0])
# (64, [1, 0, 0, 1, 0, 0, 1, 0, 0])
# (81, [1, 0, 1, 0, 1, 0, 1, 0])
# (108, [1, 0, 1, 0, 1, 0, 1, 0, 0])
# (144, [1, 0, 1, 0, 1, 0, 0, 1, 0, 0])
# (192, [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])
# (256, [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])
# (324, [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0])
# (432, [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0])
# (576, [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])
# (768, [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])
# (1024, [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])
# (1296, [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0])
# (1728, [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])
# (2304, [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])
# (3072, [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])

import numpy as np


def loss(x):
    return np.sin(x)


def nabla(x):
    return np.cos(x)


def hessian(x):
    return -np.sin(x)


x = np.pi/2+0.1
eta = 0.001
for i in range(1000):
    print(x)

    x -= 0.0000001 * nabla(x) / hessian(x)
    print(x)
