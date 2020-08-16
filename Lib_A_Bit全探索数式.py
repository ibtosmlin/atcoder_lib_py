#!/usr/bin python3
# -*- coding: utf-8 -*-

S = input()
l = len(S)-1
for i in range(2**l):
    fs = S[0]
    for j in range(l):
        if (i>>j & 1) == 1:
            fs += '+'
        else:
            fs += '-'
        fs += S[j+1]
    if eval(fs)==7:
        ret = fs + '=7'
        break
print(ret)