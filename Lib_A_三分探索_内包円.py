#!/usr/bin python3
# -*- coding: utf-8 -*-

#######################
# 内包円
# 三分探索
# https://atcoder.jp/contests/abc151/tasks/abc151_f
#######################

n = int(input())
pt = [tuple(map(int, input().split())) for i in range(n)]

def f(x, y):
    return max([((x-u)**2 + (y-v)**2)**0.5 for u, v in pt])

d = 0.0000001

def g(x):
    low, high = 0, 1000
    for i in range(80):
        l_ = (high+2*low)/3
        h_ = (high*2+low)/3
        if f(x, h_)<f(x, l_):
            low = l_
        else:
            high = h_
    return f(x, low)


low, high = 0, 1000
for i in range(80):
    l_ = (high+2*low)/3
    h_ = (high*2+low)/3
    if g(h_)<g(l_):
        low = l_
    else:
        high = h_

print(g(low))
