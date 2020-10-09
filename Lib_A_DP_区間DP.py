#!/usr/bin python3
# -*- coding: utf-8 -*-

n = int(input())
a = list(map(int, input().split()))
INF = float('inf')

# 区間DP

# dp[l][r]   [l,r) を一体にする最低のコスト
# 一回の処理のコストは、a[r]-a[l]
dp = [[0] * (n + 1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][i] = 0

sum_a = [0] * (n+1)
for i in range(1,n+1):
    sum_a[i] += sum_a[i-1] +a[i-1]

for w in range(2, n+1):
    for l in range(0, n):
        if l + w > n:
            break
        r = l + w
        ret = INF
        for k in range(l+1, r):
            ret = min(ret, dp[l][k] + dp[k][r])
        dp[l][r] = ret + sum_a[r]-sum_a[l]
print(dp[0][n])
