#!/usr/bin python3
# -*- coding: utf-8 -*-

# 深さ優先探索

from collections import deque
mod = 10**9+7

class Tree():
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]
        self.root = None    # 根
        self.size = [1] * n # 部分木のノード数
        self.depth = [-1] * self.n
        self.par = [-1] * self.n
        self.order = [] # 深さ優先探索の行きがけ順

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def set_root(self, root):
        self.root = root        # 根を設定して
        self.depth[root] = 0    # 深さ
        self.order.append(root) # 行きがけ順を設定
        nxt_q = deque([root])
        while nxt_q:
            p = nxt_q.pop() # 深さ優先探索
            for q in self.edges[p]:
                if self.depth[q] != -1: continue
                self.par[q] = p
                self.depth[q] = self.depth[p] + 1
                self.order.append(q)
                nxt_q.append(q)
        for p in self.order[::-1]:  # 帰りがけ順で
            for q in self.edges[p]:
                if self.par[p] == q: continue
                self.size[p] += self.size[q]    # 部分木のノード数


n, m = map(int, input().split())
T = Tree(n)
for _ in range(n-1):
    a, b = map(int, input().split())
    T.add_edge(a-1, b-1)

T.set_root(0)

for x in T.order:   行きがけ順

for x in T.order[::-1]: 帰りがけ順で


from collections import deque

P = [-1] * N # P[i] はiの親。iが根なら-1
Q = deque([0]) # queue。根にするやつを最初に追加
R = [] # トポロジカルソート
while Q:
    i = deque.popleft(Q)
    R.append(i)
    for a in X[i]:
        if a == P[i]: continue
        P[a] = i
        X[a].remove(i) # ☆☆☆
        deque.append(Q, a)

print("X =", X) # 子リスト
print("P =", P) # 親
print("R =", R) # トポロジカルソート