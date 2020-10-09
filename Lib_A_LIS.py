#!/usr/bin python3
# -*- coding: utf-8 -*-

from bisect import bisect

n = int(input())
a = list(map(int, input().split()))
dp = []
# 最長増加部分列
# dp[k]
# 今まで見た来たものの中で、単調増加な部分列であって、
# 長さ k であるようなもののうち、その最後の要素の最小値
# kに対して単調増加
for ai in a:
    pos = bisect(dp, ai)
    if len(dp) <= pos:
        dp.append(ai)
    else:
        dp[pos] = ai
print(len(dp))
