#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 14:09
# @Author  : frelikeff
# @Site    : 
# @File    : makeheap.py
# @Software: PyCharm


def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2 * pos + 1  # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2 * pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)


def heapify(x):
    """Transform list into a heap, in-place, in O(len(x)) time."""
    n = len(x)
    # Transform bottom-up.  The largest index there's any point to looking at
    # is the largest with a child index in-range, so must have 2*i + 1 < n,
    # or i < (n-1)/2.  If n is even = 2*j, this is (2*j-1)/2 = j-1/2 so
    # j-1 is the largest, which is n//2 - 1.  If n is odd = 2*j+1, this is
    # (2*j+1-1)/2 = j so j-1 is the largest, and that's again n//2-1.
    for i in reversed(range(n // 2)):
        _siftup(x, i)


class MinHeap:  # 子孙<=祖先
    def __init__(self, nums=None):
        self.data = []
        self.end_idx = -1
        if not nums:
            return
        for item in nums:
            self.push(item)
        return

    def push(self, item):
        self.data.append(item)
        self.end_idx += 1
        start = self.end_idx
        while start > 0:
            parent = (start - 1) >> 1
            if self.data[start] < self.data[parent]:
                self.data[start], self.data[parent] = self.data[parent], self.data[start]
                start = parent
            else:
                break
        return

    def pop(self):
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        self.end_idx -= 1
        start = 0
        while start < (self.end_idx + 1) >> 1: # 非叶节点才需要调整，到了叶子位置就没必要了
            left = (start << 1) + 1
            right = (start + 1) << 1
            if right > self.end_idx:  # 说明没有右子节点
                if self.data[start] > self.data[self.end_idx]:
                    self.data[start], self.data[self.end_idx] = self.data[self.end_idx], self.data[start]
                break
            else:

                if self.data[right] < self.data[left]:
                    if self.data[start] > self.data[right]:
                        self.data[start], self.data[right] = self.data[right], self.data[start]
                        start=right
                    else:
                        break
                else:
                    if self.data[start] > self.data[left]:
                        self.data[start], self.data[left] = self.data[left], self.data[start]
                        start=left
                    else:
                        break
        return self.data.pop()

    def __bool__(self):
        return not self.end_idx == -1


if __name__ == '__main__':
    a = [17, 11, 15, 9, 16, 6, 13, 14, 5, 0]
    heap = MinHeap(a)
    print(heap.data)

    # print(heap.pop())
    while heap:
        print(heap.pop())
        print(heap.data)
