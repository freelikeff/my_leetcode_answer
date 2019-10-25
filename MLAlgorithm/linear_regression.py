#!D:\my_venv\Scripts python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/13 19:11
# @Author  : frelikeff
# @Site    : 
# @File    : linear_regression.py
# @Software: PyCharm
import numpy as np


# 利用正规方程解来求解参数
class LinearRgressionNormal:
    def __init__(self):
        self.b = None
        self.k = None
        self.theta = None

    def fit_normal(self, X_train, y_train):
        assert X_train.shape[0] == y_train.shape[0], "the size of X_train must be equal to the size of y_train"
        X_b = np.hstack((np.ones((len(X_train), 1)), X_train))
        self.theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)
        self.b = self.theta[0]
        self.k = self.theta[1:]


class LinearRgression:
    def __init__(self):
        self.b = None
        self.k = None
        self.theta = None
        self.X_b = None

    def fit(self, X_train, y_train,eta=0.01, n_iters=1 << 13, epsilon=0.0):
        assert X_train.shape[0] == y_train.shape[0], "the size of X_train must be equal to the size of y_train"
        self.X_b = np.hstack((np.ones((len(X_train), 1)), X_train))
        self.theta = np.random.randn(X_train.shape[1]+1)

        self._gradient_descent(y_train,eta, n_iters, epsilon)
        print("train over")
        self.b=self.theta[0]
        self.k=self.theta[1:]

    def _loss(self, y, old_theta=None):
        if old_theta is not None:
            return np.linalg.norm(self.X_b.dot(old_theta) - y) / len(y)
        return np.linalg.norm(self.X_b.dot(self.theta) - y) / len(y)

    def _nabla_loss(self, y):
        return self.X_b.T.dot(self.X_b.dot(self.theta) - y) / len(y)

    def _gradient_descent(self, y, eta, n_iters, epsilon):
        i = 0
        while i < n_iters:
            last_theta = self.theta

            grad=self._nabla_loss(y)
            self.theta -= eta*grad
            if abs(self._loss(y) - self._loss(y, last_theta)) < epsilon:
                break
            i+=1



if __name__ == '__main__':
    my_model = LinearRgression()
    X = 8 * np.random.rand(100, 3)
    y = X.dot(np.array([2, 3, 4])) + np.full(shape=(100,), fill_value=5) + np.random.rand(100, )
    print(X.shape, y.shape)
    my_model.fit(X[:80], y[:80],)
    print(my_model.theta)


    my_model = LinearRgressionNormal()

    print(X.shape, y.shape)
    my_model.fit_normal(X[:80], y[:80])
    print(my_model.theta)
    # my_model.train()
    # print(my_model.get_canshu())
    # print(my_model.predict(X[80:]))
    # my_model.evaluate(X[80:], y[80:])
    # from sklearn import datasets
