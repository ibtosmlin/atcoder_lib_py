#!/usr/bin python3
# -*- coding: utf-8 -*-

# dp[i][j] i,jまでみた時の場合の数
# dp[i][j]= dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]
# 上からくるやつと横からくるやつの合計から重複分を控除
# S[i]==T[j]と一致できるなら、dp[i-1][j-1]分だけ増加する
# https://atcoder.jp/contests/abc130/tasks/abc130_e

n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][0]=1

for i in range(n+1):
    si=s[i-1]
    dpi=dp[i-1]
    for j in range(m+1):
        dpij = dp[i][j]
        if j>=1: dpij += dp[i][j-1]
        if i>=1: dpij += dpi[j]
        if i>=1 and j>=1:
            dpij -= dpi[j-1]
            if s[i-1]==t[j-1]:
                dpij += dpi[j-1]
        dp[i][j]=dpij%1000000007

print(dp[-1][-1])
