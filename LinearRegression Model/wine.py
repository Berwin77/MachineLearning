#! /usr/bin/python
# -*- coding:utf-8 -*-
import xgboost as xgb
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


def show_accuracy(a, b, tip):
    acc = a.ravel()  == b.ravel()
    print acc
    print tip + '正确率： \t', float(acc.sum()) / a.size

if __name__ == "__main__":
    data = np.loadtxt('12.wine.data', dtype=float, delimiter=',')
    y, x = np.split(data, (1,), axis=1)
    x = StandardScaler().fit_transform(x)
    x_train , x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.5)

    lr = LogisticRegression(penalty='l2')
    lr.fit(x_train, y_train)
    y_hat = lr.predict(x_test)
    show_accuracy(y_hat, y_test,'Logistic回归')

    #Xgboost
    y_train[y_train == 3] = 0
    y_test[y_test == 3] = 0
