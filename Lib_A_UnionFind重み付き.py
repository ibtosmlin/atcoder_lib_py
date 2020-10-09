#!/usr/bin python3
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10001000)

class UnionFindWeighted:
    def __init__(self, n):                      #初期化
        self.n = n                              # 要素数
        self.parents = [i for i in range(n)]    # 親
        self.ranks = [0] * n                    # 木の深さ
        self.sizes = [1] * n                    # グループの要素数
        self.weights = [0] * n                  # 親との重み

    def find(self, x):          #親を出力
        if self.parents[x] == x:
            return x
        else:
            p = self.find(self.parents[x])
            self.weights[x] += self.weights[self.parents[x]]
            self.parents[x] = p
            return p

    def unite(self, x, y, w):          # ユニオン
        # a[x]->a[y]  の差はw  # a[y]=a[x]+w
        rx = self.find(x)
        ry = self.find(y)
        wx = self.weight(x)
        wy = self.weight(y)
        if rx == ry: return
        if self.ranks[rx] > self.ranks[ry]:
            rx , ry = ry, rx    #ryを親にする
            wx , wy = wy, wx
            w *= -1
            print("a")
        self.parents[rx] = ry
        self.sizes[ry] += self.sizes[rx]
        self.weights[rx] = wy - wx - w
        if self.ranks[rx]==self.ranks[ry]:
            self.ranks[rx] += 1

    def same(self, x, y):       #xとyが同じグループかどうか
        return self.find(x) == self.find(y)

    def members(self, x):       #xと同じグループの要素
        root = self.find(x)
        return {i for i in range(self.n) if self.find(i) == root}

    def size(self, x):          #グループの要素数
        root = self.find(x)
        return self.sizes[root]

    def roots(self):            #親の要素一覧
        return {i for i, x in enumerate(self.parents) if i == x}

    def group_count(self):      #グループの個数
        return len(self.roots())

    def all_group_members(self):      #グループのメンバー一覧
        return {r: self.members(r) for r in self.roots()}

    def weight(self, x):       #重みの差
        _ = self.find(x)
        return self.weights[x]

    def diff(self, x, y):       #重みの差
        return self.weight(y) - self.weight(x)

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

################

n, m = map(int, input().split())
uf = UnionFindWeighted(n)
for _ in range(m):
    a, b, w = map(int,input().split())
    uf.unite(a-1, b-1, w)
