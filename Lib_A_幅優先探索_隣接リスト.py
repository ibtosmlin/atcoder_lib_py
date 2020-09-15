#!/usr/bin python3
# -*- coding: utf-8 -*-

# 双方向グラフで幅優先探索

from collections import deque

n, m = map(int, input().split())
g = [[] for _ in range(n)]
#隣接リストの作成
for i in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    g[a].append(b)
    g[b].append(a)
#    print(g)
#幅優先探索
q = deque()
seen = [False]*n
level = [-1]*n
parent = [-1]*n
q.append(0)
seen[0] = True
level[0] = 0
parent[0] = 0
while len(q)>0:
    cur = q.popleft()
    lvl = level[cur]
    for i in g[cur]:
        if seen[i]==False:
            seen[i] = True
            #階層
            level[i] = lvl + 1
            #親
            parent[i] = cur
            q.append(i)
#    print(seen)
#    print(level)
#    print(parent)
