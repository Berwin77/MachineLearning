# !/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib as mpl
import pydotplus
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

def iris_type(s):
    it = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
    return it[s]

if __name__ == "__main__":
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    path = '8.iris.data'
    data = np.loadtxt(path, dtype=float, delimiter=',', converters={4: iris_type})
    x, y = np.split(data, (4,), axis=1)
    # print x,y
    x = x[:, :2]

    #数据进行分组
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state= 2)
    # print x_train
    # print '================================='
    # print y_train

    model = Pipeline([
                      ('ss', StandardScaler()),
                      ('DTC', DecisionTreeClassifier(criterion='entropy', max_depth=3))])

    model = model.fit(x_train, y_train)


    # ss = StandardScaler()
    # ss = ss.fit_transform(x_train)
    # model = DecisionTreeClassifier(criterion='entropy', max_depth=3)
    # model = model.fit(x_train, y_train)

    y_test_hat = model.predict(x_test)

    #存成可视化的决策树文件

    f = open('.\\iris_tree2017.dot', 'w')
    tree.export_graphviz(model.get_params('DTC')['DTC'], out_file=f)
    f.close()

    #画图
    N,M = 100, 100
    x1_min, x1_max = x[:, 0].min(), x[:,0].max()
    x2_min, x2_max = x[:, 1].min(), x[:,1].max()
    t1 = np.linspace(x1_min, x1_max, N)
    t2 = np.linspace(x2_min, x2_max, M)
    x1, x2 = np.meshgrid(t1, t2)
    print x1
    print '------'
    print x2
    # x_show = np.stack((x1.flat, x2.flat), axis =1)








