#!/usr/bin python3
# -*- coding: utf-8 -*-

# 双方向グラフで深さ優先探索

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
#深さ優先探索
seen = [False]*N
ret = 0
for st in range(N):
    db = set([])
    if seen[st]==True:
        continue
    level = [-1]*N
    q = deque([])
    q.append(st)
    lvl = 0
    while len(q)>0:
        cur = q.pop()
        if seen[cur] == False:
            seen[cur] = True
            level[cur] = lvl
            lvl += 1
        else:
            db.add(cur)
        for i in graph[cur]:
            if seen[i]==False:
                q.append(i)
    ret += (len(db)==0)
print(ret)
