# !/usr/bin/python
# -*- coding:utf-8 -*-

import math
import matplotlib.pyplot as plt
import numpy as np
import codecs
import random






def save_parameter(pi, A, B, time):
    f_pi = open(".\\pi%d.txt" % time, "w")
    list_write(f_pi, pi)
    f_pi.close()
    f_A = open(".\\A%d.txt" % time, "w")
    for a in A:
        list_write(f_A, a)
    f_A.close()
    f_B = open(".\\B%d.txt" % time, "w")
    for b in B:
        list_write(f_B, b)
    f_B.close()




def load_train():
    f = file(".\\pi.txt", mode="r")
    for line in f:
        pi = map(float, line.split(' ')[:-1])
    f.close()

    f = file(".\\A.txt", mode="r")
    A = [[] for x in range(4)] # 转移矩阵：B/M/E/S
    i = 0
    for line in f:
        A[i] = map(float, line.split(' ')[:-1])
        i += 1
    f.close()

    f = file(".\\B.txt", mode="r")
    B = [[] for x in range(4)]
    i = 0
    for line in f:
        B[i] = map(float, line.split(' ')[:-1])
        i += 1
    f.close()
    return pi, A, B


def viterbi(pi, A, B, o):
    T = len(o)   # 观测序列
    delta = [[0 for i in range(4)] for t in range(T)]
    pre = [[0 for i in range(4)] for t in range(T)]  # 前一个状态   # pre[t][i]：t时刻的i状态，它的前一个状态是多少
    for i in range(4):
        delta[0][i] = pi[i] + B[i][ord(o[0])]
    for t in range(1, T):
        for i in range(4):
            delta[t][i] = delta[t-1][0] + A[0][i]
            for j in range(1,4):
                vj = delta[t-1][j] + A[j][i]
                if delta[t][i] < vj:
                    delta[t][i] = vj
                    pre[t][i] = j
            delta[t][i] += B[i][ord(o[t])]
    decode = [-1 for t in range(T)]  # 解码：回溯查找最大路径
    q = 0
    for i in range(1, 4):
        if delta[T-1][i] > delta[T-1][q]:
            q = i
    decode[T-1] = q
    for t in range(T-2, -1, -1):
        q = pre[t+1][q]
        decode[t] = q
    return decode


def segment(sentence, decode):
    N = len(sentence)
    i = 0
    while i < N:  #B/M/E/S
        if decode[i] == 0 or decode[i] == 1:  # Begin
            j = i+1
            while j < N:
                if decode[j] == 2:
                    break
                j += 1
            print sentence[i:j+1], "|",
            i = j+1
        elif decode[i] == 3 or decode[i] == 2:    # single
            print sentence[i:i+1], "|",
            i += 1
        else:
            print 'Error:', i, decode[i]
            i += 1


if __name__ == "__main__":
    pi, A, B = load_train()
    f = file("Spring.txt")
    data = f.read()[3:].decode('utf-8')
    f.close()
    decode = viterbi(pi, A, B, data)
    segment(data, decode)
