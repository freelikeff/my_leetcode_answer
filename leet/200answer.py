#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 10:00
# @Author  : frelikeff
# @Site    : 
# @File    : 200answer.py
# @Software: PyCharm
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height, width = len(grid), len(grid[0])
        ans = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "0":
                    continue
                stack = [(i, j)]
                grid[i][j] = "0"
                while stack:

                    temp_i, temp_j = stack.pop()
                    if temp_i > 0 and grid[temp_i - 1][temp_j] == "1":
                        stack.append((temp_i - 1, temp_j))
                        grid[temp_i - 1][temp_j] = "0"

                    if temp_j > 0 and grid[temp_i][temp_j - 1] == "1":
                        stack.append((temp_i, temp_j - 1))
                        grid[temp_i][temp_j - 1] = "0"

                    if temp_j < width - 1 and grid[temp_i][temp_j + 1] == "1":
                        stack.append((temp_i, temp_j + 1))
                        grid[temp_i][temp_j + 1] = "0"

                    if temp_i < height - 1 and grid[temp_i + 1][temp_j] == "1":
                        stack.append((temp_i + 1, temp_j))
                        grid[temp_i + 1][temp_j] = "0"

                ans += 1
        return ans


# 并查集
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        class UnionFindSet():
            def __init__(self, n):
                self.parent = [i for i in range(n)]  #
                self.count = n

            def get_root(self, p):
                while p != self.parent[p]:
                    p = self.parent[p]
                return p

            def union(self, p, q):
                p_root = self.get_root(p)
                q_root = self.get_root(q)
                if p_root == q_root:
                    return
                self.parent[p_root] = q_root
                self.count -= 1

            def get_count(self):
                return self.count

        height, width = len(grid), len(grid[0])

        my_uf = UnionFindSet(height * width + 1)  # 所有的水连接到最后一个里面
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "1":
                    if i < height - 1 and grid[i + 1][j] == "1":
                        my_uf.union(i * width + j, (i + 1) * width + j)
                    if j < width - 1 and grid[i][j + 1] == "1":
                        my_uf.union(i * width + j, i * width + j + 1)
                else:
                    my_uf.union(i * width + j, height * width)
        return my_uf.get_count()-1


if __name__ == '__main__':
    s = Solution()
    inpt = [["1", "0", "1", "1", "1"], ["1", "0", "1", "0", "1"], ["1", "1", "1", "0", "1"]]
    ans = s.numIslands(inpt)
    print(ans)
