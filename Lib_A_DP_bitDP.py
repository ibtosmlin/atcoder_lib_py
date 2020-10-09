#!/usr/bin python3
# -*- coding: utf-8 -*-

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

# bitDP
# https://atcoder.jp/contests/dp/tasks/dp_u
# dp[S]:集合Sに対しての最大値をdpとする
# dp[S]= max(dp[v:=S-u] + dp[u])  uはSの部分集合

dp = [0] * (2**n)

cost = [0] * (2**n)
for s in range(2**n):
    for i in range(n):
        if s>>i & 1:
            for j in range(i+1, n):
                if s>>j & 1:
                    cost[s] += a[i][j]

for s in range(1, 2**n):
    u = s   #sの部分集合
    while True:
        dp[s] = max(dp[s], dp[s-u] + cost[u])
        u = (u-1) & s   #次のsの部分集合
        if u == s: break

print(dp[-1])