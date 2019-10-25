#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/3 14:59
# @Author  : frelikeff
# @Site    : 
# @File    : pca.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt


def demean(X):
    return X - X.mean(axis=0)


def direction(w):  # 将向量单位化
    return w / np.linalg.norm(w)


def D(w, X):  # 映射至w方向上的方差
    return np.sum(X.dot(w) ** 2) / len(x)


def nabla_D(w, X):
    return 2 / len(X) * X.T.dot(X).dot(w)


def gradient_ascent(X, w=None, n_iters=1e4, eta=0.001, epsilon=1e-8):
    if w is None:
        w = np.random.randn(x.shape[1])
    cur_iter = 0
    while cur_iter < n_iters:
        grad = nabla_D(w, x)
        last_w = w
        w += eta * grad
        w = direction(w)
        if abs(D(last_w, X) - D(w, x)) < epsilon:
            break
        cur_iter += 1

    return w


if __name__ == '__main__':
    x = np.empty((100, 2))
    x[:, 0] = np.random.uniform(0, 100, size=100)
    x[:, 1] = 0.75 * x[:, 0] + 3 + np.random.normal(0, 1, size=100)
    x = demean(x)

    ans = gradient_ascent(x)
    print(ans[1] / ans[0])
    print(ans)

    plt.scatter(x[:, 0], x[:, 1])
    plt.plot([0, ans[0] * 50], [0, ans[1] * 50], color="red")
    plt.show()
