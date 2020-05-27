#!/usr/bin python3
# -*- coding: utf-8 -*-

# 双方向グラフで深さ優先探索(再帰)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
seen = [False]*N

# 隣接リストの作成
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

# 深さ優先探索
def dfs(g,v):
    seen[v] = True
    for nv in g[v]:
        if seen[nv] == True: continue
        dfs(g,nv)

def main():
    start = 0
    stcol = 1
    dfs(graph, start, stcol)
    print(seen)

if __name__ == '__main__':
    main()