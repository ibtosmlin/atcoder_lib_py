#!/usr/bin python3
# -*- coding: utf-8 -*-

# 双方向グラフで幅優先探索

from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
#隣接リストの作成
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
#    print(graph)
#幅優先探索
q = deque()
seen = [False]*N
level = [-1]*N
parent = [-1]*N
q.append(0)
seen[0] = True
level[0] = 0
parent = 0
while len(q)>0:
    cur = q.popleft()
    lvl = level[cur]
    for i in graph[cur]:
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
