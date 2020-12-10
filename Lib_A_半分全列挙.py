#!/usr/bin python3
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc184/tasks/abc184_f

# 半分全列挙
# n <= 40 だと半分で全列挙したものをそれぞれ計算してマージ処理する

n, t = map(int, input().split())
v = list(map(int, input().split()))

def get_list(vl):
    ret = [0]
    svl = sorted(vl)
    for vi in svl:
        for j in range(len(ret)):
            x = vi + ret[j]
            if x > t: continue
            ret.append(x)
    return sorted(ret)

former = get_list(v[:n//2])
latter = get_list(v[n//2:])

ret = 0
up = len(latter) - 1
for f in former:
    while up >= 0 and (latter[up]+f) > t:
        up -= 1
    ret = max(ret, latter[up]+f)

print(ret)
