#!/usr/bin python3
# -*- coding: utf-8 -*-

class UnionFind():
    def __init__(self, n):      #初期化
        self.n = n
        # 親
        self.parents = [i for i in range(n)]
        # 木の深さ
        self.ranks = [0] * n
        # グループの要素数
        self.sizes = [1] * n

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
            self.sizes[y] += self.sizes[x]
        else:
            self.parents[y] = x
            self.sizes[x] += self.sizes[y]
            if self.ranks[x]==self.ranks[y]:
                self.ranks[x] += 1

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

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

################

def main():
    N, M = map(int, input().split())
    uf = UnionFind(N)
    for i in range(M):
        a,b = map(int,input().split())
        uf.unite(a-1, b-1)

    print(uf.group_count())


if __name__ == '__main__':
    main()