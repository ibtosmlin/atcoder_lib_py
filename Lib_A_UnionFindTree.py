#!/usr/bin python3
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/atc001/tasks/unionfind_a

import sys
sys.setrecursionlimit(10001000)

class UnionFind:
    def __init__(self, n):                      #初期化
        self.n = n                              # 要素数
        self.parents = [i for i in range(n)]    # 親
        self.ranks = [0] * n                    # 木の深さ
        self.sizes = [1] * n                    # グループの要素数

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
        self.sizes[y] += self.sizes[x]

    def same(self, x, y):       #xとyが同じグループかどうか
        return self.find(x) == self.find(y)

    def members(self, x):       #xと同じグループの要素
        root = self.find(x)
        return {i for i in range(self.n) if self.find(i) == root}

    def size(self, x):          #グループの要素数
        return self.sizes[self.find(x)]

    def roots(self):            #親の要素一覧
        return {i for i, x in enumerate(self.parents) if i == x}

    def group_count(self):      #グループの個数
        return len(self.roots())

    def all_group_members(self):      #グループのメンバー一覧
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

################

n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
    a,b = map(int,input().split())
    uf.unite(a-1, b-1)

print(uf.group_count())
print(uf.same(1,2))
