#!/usr/bin python3
# -*- coding: utf-8 -*-

# 深さ優先探索
# 双方向グラフ
# 行きかけ、帰りがけ処理

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

# dp[i][j]  node i でj=0白の個数,j=1黒の個数
dp = [[-1]*2 for _i in range(n)]

# 深さ優先探索（行きがけ1、帰りがけ0処理）
seen = [False] * n
q = deque([(0, 0),(1, 0)])
while len(q)>0:
    fg, node = q.pop()
#    print(fg, node)
    if fg:  #行き掛け
        seen[node] = True
        for nxt in g[node]:
            if seen[nxt]: continue
            q.append((0, nxt))
            q.append((1, nxt))
    else:   #帰り掛け
        dp[node][0] = 1
        dp[node][1] = 1
        for child in g[node]:
            w, b = dp[child]
            if w == -1: continue
            dp[node][0] *= (w + b)
            dp[node][0] %= mod
            dp[node][1] *= w
            dp[node][1] %= mod
print(sum(dp[0])%mod)
#print(dp)