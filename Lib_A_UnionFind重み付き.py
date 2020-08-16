#!/usr/bin python3
# -*- coding: utf-8 -*-

class UnionFindWeighted():
    def __init__(self, n):      #初期化
        self.n = n
        # 親
        self.parents = [i for i in range(n)]
        # 木の深さ
        self.ranks = [0] * n
        # グループの要素数
        self.sizes = [1] * n
        # 重み
        self.weights = [0] * n

    def find(self, x):          #親を出力
        if self.parents[x] == x:
            return x
        else:
            y = self.find(self.parents[x])
            self.weights[x] = self.weights[self.parents[x]]
            self.parents[x] = y
            return y

    def unite(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)

        if self.ranks[rx] < self.ranks[ry]:
            self.parents[rx] = ry
            self.sizes[ry] += self.sizes[rx]
            self.weights[rx] = w - self.weights[x] + self.weights[y]
        else:
            self.parents[ry] = rx
            self.sizes[rx] += self.sizes[ry]
            self.weights[ry] = - w - self.weights[y] + self.weights[x]
            if self.ranks[rx]==self.ranks[ry]:
                self.ranks[rx] += 1
        print(self.weights)

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

    def diff(self, x, y):      #重みの差
        return self.weights[x] - self.weights[y]

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

################

N, M = map(int, input().split())
uf = UnionFindWeighted(N)
for i in range(M):
    a,b,w = map(int,input().split())
    uf.unite(a-1, b-1, w)
