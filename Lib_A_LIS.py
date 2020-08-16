#!/usr/bin python3
# -*- coding: utf-8 -*-

from bisect import bisect

N = int(input())
A = list(map(int, input().split()))
dp = []
# dp[k]
# 今まで見た来たものの中で、単調増加な部分列であって、
# 長さ k であるようなもののうち、その最後の要素の最小値
# kに対して単調増加
for a in A:
    pos = bisect(dp, a)
    if len(dp) <= pos:
        dp.append(a)
    else:
        dp[pos] = a
print(len(dp))
