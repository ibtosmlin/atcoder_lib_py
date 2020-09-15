#!/usr/bin python3
# -*- coding: utf-8 -*-

# 二部グラフを判定する

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

colors = [0 for i in range(n)]

#2部グラフならTrue, そうでなければFalse
def is_bipartite():
    stack = [(0,1)] # (頂点、色)のタプルをスタックする。最初は(頂点0, 黒(1))
    while stack:
        #スタックから最後に追加された(頂点, 色)をpop
        v, color = stack.pop()
        #今いる点を着色
        colors[v] = color
        #今の頂点から行けるところをチェック
        for to in graph[v]:
            #同じ色が隣接してしまったらFalse
            if colors[to] == color:
                return False
            #未着色の頂点があったら反転した色と共にスタックに積む
            if colors[to] == 0:
                stack.append((to, -color))
    #調べ終わったら矛盾がないのでTrue
    return True
