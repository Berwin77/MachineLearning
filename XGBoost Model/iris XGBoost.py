#! /usr/bin/python
# -*- coding:utf-8 -*-

import xgboost as xgb
import numpy as np
from sklearn.model_selection import train_test_split

def iris_type(s):
    it = {'Iris-setosa':0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
    return it[s]

if __name__ == "__main__":
    path = '8.iris.data'
    data = np.loadtxt(path, dtype=float, delimiter=',', converters={4: iris_type})
    x, y =np.split(data, (4,), axis=1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, train_size=50)

    data_train = xgb.DMatrix(x_train, y_train)
    data_test = xgb.DMatrix(x_test, y_test)
    watch_list = [(data_test,'eval'), (data_train, 'train')]
    param = {'max_depth': 3, 'eta': 1, 'silent': 1, 'objective': 'multi:softmax', 'num_class': 3}
    bst = xgb.train(param, data_train, num_boost_round=6, evals=watch_list)

    y_hhat = bst.predict(data_train)
    resu = y_train.reshape(1,-1)
    print y_hhat
    print resu
    # print'训练集的正确率：' , float(np.sum(resu)) / len(y_hhat)
    print '==========================================================='
    y_hat = bst.predict(data_test)
    result = y_test.reshape(1, -1) == y_hat

    print '测试集正确率为：', float(np.mean(result)) / len(y_hat)
    print 'END..................\n'