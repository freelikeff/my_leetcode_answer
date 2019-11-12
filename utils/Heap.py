#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 9:18
# @Author  : frelikeff
# @Site    : 
# @File    : Heap.py
# @Software: PyCharm

class MinHeap:
    def __init__(self):
        self.nums = []
        self.size = 0

    def push(self, value):
        self.nums.append(value)

        idx = self.size
        father = (idx - 1) >> 1
        while idx and self.nums[idx] < self.nums[father]:
            self.nums[idx], self.nums[father] = self.nums[father], self.nums[idx]
            idx = father
            father = (idx - 1) >> 1

        self.size += 1
        return

    def pop(self):
        if self.size < 3:
            self.size -= 1
            return self.nums.pop(0)

        ans = self.nums[0]
        self.nums[0] = self.nums.pop()
        self.size -= 1

        idx = 0
        left, right = (idx << 1) + 1, (idx + 1) << 1
        while right < self.size:
            # 先确定孩子中的最小值
            if self.nums[left] >= self.nums[right]:
                minn, maxx = right, left
            else:
                minn, maxx = left, right

            # 如果比孩子大，那么就需要下沉
            if self.nums[idx] > self.nums[minn]:
                self.nums[idx], self.nums[minn] = self.nums[minn], self.nums[idx]
                idx = minn
                left, right = (idx << 1) + 1, (idx + 1) << 1
            # 到位了直接return
            else:
                return ans

        if left < self.size:
            if self.nums[idx] > self.nums[left]:
                self.nums[idx], self.nums[left] = self.nums[left], self.nums[idx]

        return ans

    def __bool__(self):
        return self.size != 0


class MaxHeap:
    def __init__(self):
        self.nums = []
        self.size = 0

    def push(self, value):
        self.nums.append(value)
        idx = self.size
        father = (idx - 1) >> 1
        while idx and self.nums[idx] > self.nums[father]:
            self.nums[idx], self.nums[father] = self.nums[father], self.nums[idx]
            idx = father
            father = (idx - 1) >> 1
        self.size += 1

    def pop(self):
        if self.size < 3:
            self.size -= 1
            return self.nums.pop(0)

        ans = self.nums[0]
        self.nums[0] = self.nums.pop()
        self.size -= 1

        idx = 0
        left, right = (idx << 1) + 1, (idx + 1) << 1
        while right < self.size:

            if self.nums[left] >= self.nums[right]:
                minn, maxx = right, left
            else:
                minn, maxx = left, right

            if self.nums[idx] < self.nums[maxx]:
                self.nums[idx], self.nums[maxx] = self.nums[maxx], self.nums[idx]
                idx = maxx
                left, right = (idx << 1) + 1, (idx + 1) << 1
            else:
                return ans
        if left < self.size:
            if self.nums[idx] < self.nums[left]:
                self.nums[idx], self.nums[left] = self.nums[left], self.nums[idx]

        return ans

    def __bool__(self):
        return self.size != 0


# 当然利用最小堆就可以封装一个最大堆
class BHeap:
    def __init__(self):
        self.memo = MinHeap()

    def push(self, value):
        self.memo.push(-value)

    def pop(self):
        return -self.memo.pop()

    def __bool__(self):
        return bool(self.memo)


if __name__ == '__main__':
    heap = BHeap()
    for item in [17, 11, 15, 9, 16, 6, 13, 14, 5, 0]:
        heap.push(item)

    while heap:
        print(heap.pop())
