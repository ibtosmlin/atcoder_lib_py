#!/usr/bin python3
# -*- coding: utf-8 -*-

# 深さ優先探索
# 隣接リスト
# 非再帰

from collections import deque

mod = 10**9+7
n = int(input())
edges = [[] for _ in range(n)]
# 隣接リストの作成
for i in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)


dp = [-1] * n       # dp[n] 深さ
parents = [-1] * n  # parents[n] 親

# 深さ優先探索
seen = [False] * n
q = deque([0])
dp[0] = 0
while len(q)>0:
    p = q.pop()
    seen[p] = True
    nw = dp[p]
    for nxt in edges[p]:
        if seen[nxt]: continue
        q.append(nxt)
        dp[nxt] = nw + 1
        parents[nxt] = p
print(dp[0])
#print(dp)