#!/usr/bin python3
# -*- coding: utf-8 -*-

# 深さ優先探索
# 双方向グラフ
# 再帰
# なんかやってから先に行く行き掛け処理

import sys
sys.setrecursionlimit(10**9)

def dfs(cur, last):
    dp[cur] = dp[last] + 1
    for nxt in g[cur]:
        if nxt == last: continue
        dfs(nxt, cur)
##################

mod = 10**9+7

#n, m = map(int, input().split())
n = int(input())
m = n-1
g = [[] for _ in range(n)]

# 隣接リストの作成
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

# 深さ優先探索
dp = [0] * n

start = 0
prev = -1
dfs(start, prev)

print(dp)