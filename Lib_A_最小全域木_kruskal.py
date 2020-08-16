#!/usr/bin python3
# -*- coding: utf-8 -*-

# 最小全域木　クラスカル法
# 重み付き無向グラフで、それらの全ての頂点を結び連結するような木の最小のコストを求める
# 辺の重みの小さい順にみて、連結成分が閉路にならない辺を追加していく
# つなぐ頂点が同じ連結成分にないことをUnion Find Tree でみる

INF = float('inf')

class UnionFind():
    def __init__(self, n):      #初期化
        self.n = n
        # 親
        self.parents = [i for i in range(n)]
        # 木の深さ
        self.ranks = [0] * n

    def find(self, x):          #親を出力
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.ranks[x] < self.ranks[y]:
            self.parents[x] = y
        else:
            self.parents[y] = x
            if self.ranks[x]==self.ranks[y]:
                self.ranks[x] += 1

    def same(self, x, y):       #xとyが同じグループかどうか
        return self.find(x) == self.find(y)

def kruskal(n, edges):
    uf = UnionFind(n)
    ret_weight = 0
    ret_edges = set([])
    ret_nodes = set([])
    for w, u, v in edges:
        if not uf.same(u, v):
            uf.unite(u, v)
            ret_weight += w
            ret_edges.add((u,v))
            ret_nodes.add(u)
            ret_nodes.add(v)
    return ret_weight

################################

N, M = map(int,.input().split())
#リストの作成
Edges = []
for i in range(M):
    a, b, w = map(int, input().split())
    Edges.append((w,a-1,b-1))
Edges.sort()

print(kruskal(N, Edges))
