#!/usr/bin python3
# -*- coding: utf-8 -*-

# 二分グラフ

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
seen = [False]*N
color = [-1]*N

# 隣接リストの作成
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

# 深さ優先探索
def dfs(g,v,c):
    seen[v] = True
    color[v] = c
    for nv in g[v]:
        # すでに隣接の色が確定していて同じ色となっている場合終了
        if seen[nv] == True:
            if color[nv]==c:
                return False
            continue
        # 隣接の色が確定していていない場合、先に進めた結果を返す
        if not dfs(g,nv,1-c):
            return False
    return True

def main():
    ret = True
    for i in range(N):
        if seen[i] == True: continue
        if dfs(graph, i, col): ret = False

    print(seen)
    print(color)

if __name__ == '__main__':
    main()