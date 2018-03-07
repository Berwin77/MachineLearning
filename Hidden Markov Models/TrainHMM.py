# !/usr/bin/python
# -*- coding:utf-8 -*-

import math
import matplotlib.pyplot as plt
import numpy as np
import codecs
import random

infinite = float(-2**10)


def log_normalize(a):
    s = 0
    for x in a:
        s += x
    if s == 0:
        print "Error..from log_normalize."
        return
    s = math.log(s)
    for i in range(len(a)):
        if a[i] == 0:
            a[i] = infinite
        else:
            a[i] = math.log(a[i]) - s






def mle():  # 0B/1M/2E/3S
    pi = [0] * 4   # npi[i]：i状态的个数
    a = [[0] * 4 for x in range(4)]     # na[i][j]：从i状态到j状态的转移个数
    b = [[0]* 65536 for x in range(4)]  # nb[i][o]：从i状态到o字符的个数
    f = file(".\\pku_training.utf8")
    data = f.read()[3:].decode('utf-8')
    f.close()
    tokens = data.split('  ')
    last_q = 2
    iii = 0
    old_progress = 0
    print '进度：'
    for k, token in enumerate(tokens):
        progress = float(k) / float(len(tokens))
        if progress > old_progress + 0.1:
            print '%.3f' % progress
            old_progress = progress
        token = token.strip()
        n = len(token)
        if n <= 0:
            continue
        if n == 1:
            pi[3] += 1
            a[last_q][3] += 1   # 上一个词的结束(last_q)到当前状态(3S)
            b[3][ord(token[0])] += 1
            last_q = 3
            continue
        # 初始向量
        pi[0] += 1
        pi[2] += 1
        pi[1] += (n-2)
        # 转移矩阵
        a[last_q][0] += 1
        last_q = 2
        if n == 2:
            a[0][2] += 1
        else:
            a[0][1] += 1
            a[1][1] += (n-3)
            a[1][2] += 1
        # 发射矩阵
        b[0][ord(token[0])] += 1
        b[2][ord(token[n-1])] += 1
        for i in range(1, n-1):
            b[1][ord(token[i])] += 1
    # 正则化
    log_normalize(pi)
    for i in range(4):
        log_normalize(a[i])
        log_normalize(b[i])
    return [pi, a, b]


def list_write(f, v):
    for a in v:
        f.write(str(a))
        f.write(' ')
    f.write('\n')


def save_parameter(pi, A, B):
    f_pi = open(".\\pi.txt", "w")
    list_write(f_pi, pi)
    f_pi.close()
    f_A = open(".\\A.txt", "w")
    for a in A:
        list_write(f_A, a)
    f_A.close()
    f_B = open(".\\B.txt", "w")
    for b in B:
        list_write(f_B, b)
    f_B.close()


if __name__ == "__main__":
    pi, A, B = mle()
    save_parameter(pi, A, B)
    print "训练完成..."
