#!/usr/bin python3
# -*- coding: utf-8 -*-

# 双方向グラフで深さ優先探索(再帰)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

# 隣接リストの作成
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

# 深さ優先探索
def dfs(cur, prev):
    ret = 0
    for nxt in graph[cur]:
        if nxt == prev:
            continue
        ret = max(ret, dfs(nxt,cur) + 1)    #例：下の階層の結果+1 との比較level
    return ret

##################

start = 0
previ = -1
print(dfs(start, previ))
