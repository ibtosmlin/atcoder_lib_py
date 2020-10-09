#!/usr/bin python3
# -*- coding: utf-8 -*-

# 最小全域木 クラスカル法
# 重み付き無向グラフで、それらの全ての頂点を結び連結するような木の最小のコストを求める
# 辺の重みの小さい順にみて、連結成分が閉路にならない辺を追加していく
# つなぐ頂点が同じ連結成分にないことをUnion Find Tree でみる

INF = float('inf')

class UnionFind():
    def __init__(self, n):      #初期化
        self.n = n                              # 要素数
        self.parents = [i for i in range(n)]    # 親
        self.ranks = [0] * n                    # 木の深さ

    def find(self, x):              # 親を出力
        if self.parents[x] == x:
            return x
        else:
            p = self.find(self.parents[x])
            self.parents[x] = p
            return p

    def unite(self, x, y):          # ユニオン
        x = self.find(x)
        y = self.find(y)
        if x == y: return
        if self.ranks[x] > self.ranks[y]:
            x , y = y, x    #yを親にする
        if self.ranks[x] == self.ranks[y]:
                self.ranks[y] += 1
        self.parents[x] = y

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
            ret_edges.add((u, v))
            ret_nodes.add(u)
            ret_nodes.add(v)
    return ret_weight

################################

n, m = map(int, input().split())
#リストの作成
Edges = []
for i in range(m):
    a, b, w = map(int, input().split())
    Edges.append((w, a-1, b-1))
Edges.sort()

print(kruskal(n, Edges))
