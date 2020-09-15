#!/usr/bin python3
# -*- coding: utf-8 -*-

# ワーシャルフロイド法
# 全頂点間最短路
# d[i][j]は2頂点間i, j間の移動コストを格納, Mは頂点数

from scipy.sparse.csgraph import floyd_warshall

INF = float("inf")

n, m = map(int,input().split()) #N:頂点数 M:辺の数
d = [[INF] * n for i in range(n)]
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(m):
    u, v, w = map(int,input().split())
    d[u-1][v-1] = w
    d[v-1][u-1] = w
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０

print(floyd_warshall(d))   #d[i][j]に頂点i, j間の最短距離を格納


# 経路復元
fwd = floyd_warshall(d)

def path(s, g):
    ret = []
    if s == g or fwd[s][g] == INF:
        return ret
    cur = s
    while cur!=g:
        for nxt in range(n):
            if nxt==cur or nxt==s: continue
            if d[cur][nxt] + fwd[nxt][g] == fwd[cur][g]:
                ret.append((cur, nxt))
#                ret.append((nxt, cur))
                cur = nxt
                break
    return ret

print(path(0, n-1))
