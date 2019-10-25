#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/1 14:57
# @Author  : frelikeff
# @Site    : 
# @File    : logisitic_regression.py
# @Software: PyCharm

import numpy as np


class LogisiticRegression:
    def __init__(self):
        self.coef_ = None
        self.intercept = None
        self.theta = None

    def _sigmoid(self, t):
        return 1 / (1 + np.exp(-t))

    def fit(self, X_train, y_train, eta=0.001, n_iters=1e4):
        """全量梯度下降"""
        assert X_train.shape[0] == y_train.shape[0], "the size of X_train must be equal to the size of y_train"

        def loss(theta, X_b, y):
            y_hat = self._sigmoid(X_b.dot(theta))
            try:
                return -np.sum(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat)) / len(y)
            except:
                return float("inf")

        def nabla_loss(theta, X_b, y):
            return X_b.T.dot(self._sigmoid(X_b.dot(theta)) - y) / len(y)

        def gradient_descent(X_b, y, initial_theta, eta, n_iters=1e4, epsilon=0.001):
            theta = initial_theta
            cur_iter = 0
            while cur_iter < n_iters:
                gradient = nabla_loss(theta, X_b, y)
                last_theta = theta
                theta = theta - eta * gradient
                if abs(loss(theta, X_b, y) - loss(last_theta, X_b, y)) < epsilon:
                    break
                cur_iter += 1

            return theta

        X_b = np.hstack((np.ones((len(X_train), 1)), X_train))
        initial_theta = np.random.randn(X_b.shape[1])
        self.theta = gradient_descent(X_b, y, initial_theta, eta, n_iters=1e4, epsilon=0.001)

        return

    def predict_proba(self, X_predict):

        assert self.theta, "must be fit before predict"
        assert X_predict.shape[1] == len(self.theta) - 1, "the feature number of predata must be equal to traindata"

        X_b_predict = np.hstack((np.ones((len(X_predict), 1)), X_predict))
        return self._sigmoid(X_b_predict.dot(self.theta))

    def predict(self, X_predict):
        assert self.theta, "must be fit before predict"
        assert X_predict.shape[1] == len(self.theta) - 1, "the feature number of predata must be equal to traindata"

        X_b_predict = np.hstack(np.ones((len(X_predict), 1)), X_predict)
        proba = self._sigmoid(X_b_predict.dot(self.theta))
        return np.array(proba > 0.5, dtype=np.int)

    def __repr__(self):
        return "LogisiticRegression"


if __name__ == '__main__':
    from sklearn import datasets
    import matplotlib.pyplot as plt

    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # 二分类，可视化，所以只取两个特征，两个类别
    X = X[y < 2, :2]
    y = y[y < 2]
    plt.scatter(X[y == 0, 0], X[y == 0, 1], color="red")
    plt.scatter(X[y == 1, 0], X[y == 1, 1], color="blue")
    plt.show()
    model = LogisiticRegression()
    model.fit(X, y)
