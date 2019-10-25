#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/1 9:11
# @Author  : frelikeff
# @Site    : 
# @File    : topological_sorting.py
# @Software: PyCharm
from typing import List



def topo_sort(n,nums: List[List[int]]) -> List[int]:
    """
    :param n: 表示课程数，从0开始编号
    :param nums: 表示依赖关系，[a,b]表示a依赖于b，也就是说b必须在a的前面
    :return: 表示排序后的结果
    """
    ans=[]
    indegree=[0 for _ in range(n)] # 表示第i个节点的入度
    relyon=[set() for _ in range(n)] # 表示第i 个节点后面都有哪些
    for front,behind in nums:
        indegree[front]+=1
        relyon[behind].add(front)

    deque=[i for i in range(n) if not indegree[i]]
    while deque:
        study=deque.pop(0)
        ans.append(study)
        for item in relyon[study]:
            indegree[item]-=1
            if not indegree[item]:
                deque.append(item)

    if len(ans)==n:
        return ans
    else:
        return []


if __name__ == '__main__':
    pass
