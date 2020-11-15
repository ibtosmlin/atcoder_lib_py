#!/usr/bin python3
# -*- coding: utf-8 -*-

# 巡回セールスマン問題
# dist部分をダイクストラで求めると一般化できる


n = int(input())
x = [list(map(int,input().split())) for _ in range(n)]
INF = float('inf')

dist = [[INF] * n for _ in range(n)]

def d(fm, to):
    if dist[fm][to] != INF:
        return dist[fm][to]
    else:
        a, b, c = x[fm]
        p, q, r = x[to]
        dist[fm][to] = abs(a-p) + abs(b-q) + max(0, r-c)
        return dist[fm][to]


# dp[s][i]  集合sに行って、今iにいる場合の最小距離
dp = [[INF]*n for _ in range(1<<n)]
dp[1][0] = 0

for s in range(1<<n):
    for fm in range(n):
        if dp[s][fm] == INF: continue
        if not s >> fm & 1: continue
        for to in range(n):
            if not s >> fm & 1: continue
            if fm==to: continue
            dp[s|1<<to][to] = min(dp[s|1<<to][to], dp[s][fm] + d(fm, to))

print(dp[-1][0])
