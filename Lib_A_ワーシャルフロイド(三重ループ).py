#!/usr/bin python3
# -*- coding: utf-8 -*-

# ワーシャルフロイド法
# 全頂点間最短路
# d[i][j]は2頂点間i, j間の移動コストを格納, Mは頂点数

def warshall_floyd(d, M):
    for k in range(M):
        for i in range(M):
            for j in range(M):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d #d[i][j]に頂点i, j間の最短距離を格納

##############################

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
    print(warshall_floyd(d,N))

if __name__ == '__main__':
    main()