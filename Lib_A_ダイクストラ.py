#!/usr/bin python3
# -*- coding: utf-8 -*-

# ダイクストラ法
# 重み付きグラフ関係により最短経路のリストを作る
# 有向グラフで優先度付きキューで探索
# https://atcoder.jp/contests/abc035/tasks/abc035_d

from heapq import heapify, heappop, heappush, heappushpop

INF = float('inf')

class dijkstra:
    def __init__(self, n, edges):
        self.n = n              # ノード数
        self.edges = edges      # 有向グラフ
        self.prev = [-1] * n    # 前のノード

    def build(self, start):
        self.dist = [INF] * self.n
        self.dist[start] = 0
        next_q = [(0, start)]
        heapify(next_q)
        while next_q:
            cd, cn = heappop(next_q)
            if self.dist[cn] < cd: continue
            for nn, nd in self.edges[cn]:
                nd_ = self.dist[cn] + nd
                if self.dist[nn] <= nd_: continue
                self.dist[nn] = nd_
                self.prev[nn] = cn
                heappush(next_q, (nd_, nn))
        return self.dist

    def shortest_distance(self, goal):
        return self.dist[goal]

    def shortest_path(self, goal):
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]


##########################################

n, m, t = map(int, input().split())
A = list(map(int,input().split()))
edges_F = [[] for _ in range(n)]
edges_R = [[] for _ in range(n)]    #行きと帰りを分けた（有向グラフ）場合
#リストの作成
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    edges_F[a].append((b,c))
    edges_R[b].append((a,c))        #行きと帰りを分けた（有向グラフ）場合

dijF = dijkstra(n, edges_F)  #クラスのインスタンス化
dijR = dijkstra(n, edges_R)
F = dijF.build(0)
R = dijR.build(0)

ret = 0
for i in range(n):
    ret = max(ret, (t-F[i]-R[i])*A[i])
print(ret)
