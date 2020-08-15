#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 10:39
# @Author  : frelikeff
# @Site    : 
# @File    : cole.py
# @Software: PyCharm


import numpy as np
import random
n=5
A=np.eye(n)
for i in range(n-1):
    A[i][i]=10*random.random()

A[n-1][n-1]=0
print(A)
B= np.random.rand(n,n-1)

V=np.random.rand(n,n)

A=V.dot(A).dot(np.linalg.inv(V))
Aeigen=np.linalg.eig(A)
print(A,B,Aeigen,sep="\n")

