#!/usr/bin python3
# -*- coding: utf-8 -*-

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def find(self, x):          #親を出力
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def same(self, x, y):       #xとyが同じグループかどうか
        return self.find(x) == self.find(y)

    def size(self, x):          #グループの要素数
        return -self.parents[self.find(x)]

    def members(self, x):       #xと同じグループの要素
        root = self.find(x)
        return {i for i in range(self.n) if self.find(i) == root}

    def roots(self):            #親の要素一覧
        return {i for i, x in enumerate(self.parents) if x < 0}

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
        a,b = map(int,input())
        uf.union(a-1, b-1)

    print(uf.group_count())


if __name__ == '__main__':
    main()