#!/usr/bin python3
# -*- coding: utf-8 -*-

# ワーシャルフロイド法
# 全頂点間最短路
# d[i][j]は2頂点間i, j間の移動コストを格納, Mは頂点数

from scipy.sparse.csgraph import floyd_warshall

def main():
    N, M = map(int,input().split()) #N:頂点数　M:辺の数
    d = [[float("inf")]*N for i in range(N)]
    #d[u][v] : 辺uvのコスト(存在しないときはinf)
    for i in range(M):
        u, v, w = map(int,input().split())
        d[u-1][v-1] = w
        d[v-1][u-1] = w
    for i in range(N):
        d[i][i] = 0 #自身のところに行くコストは０

    print(floyd_warshall(d))

if __name__ == '__main__':
    main()