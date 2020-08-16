#!/usr/bin python3
# -*- coding: utf-8 -*-

#######################
# ムーアの法則
# 三分探索
#######################

p = float(input())

def f(x):
    return x + p / pow(2, x/1.5)

d = 0.000000001
low, high = 0, 1000
while abs(f(low)-f(high))>d:
    l_ = (high+2*low)/3
    h_ = (high*2+low)/3
    if f(h_)<f(l_):
        low = l_
    else:
        high = h_
print(f(low))
