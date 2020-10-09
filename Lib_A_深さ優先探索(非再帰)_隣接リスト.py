#!/usr/bin python3
# -*- coding: utf-8 -*-

# 深さ優先探索
# 隣接リスト
# 非再帰

from collections import deque

mod = 10**9+7
n = int(input())
g = [[] for _ in range(n)]
# 隣接リストの作成
for i in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

# dp[n]  深さ
dp = [-1 for _i in range(n)]

# 深さ優先探索
seen = [False] * n
q = deque([0])
dp[0] = 0
while len(q)>0:
    node = q.pop()
    seen[node] = True
    nw = dp[node]
    for nxt in g[node]:
        if seen[nxt]: continue
        q.append(nxt)
        dp[nxt] = nw + 1
print(dp[0])
#print(dp)