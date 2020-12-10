#!/usr/bin python3
# -*- coding: utf-8 -*-

# トポロジカルソート

from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n)]  # 有向辺
in_cnt = [0] * n                # 入力
ts = []                         # トポロジカルソート
parents = [-1] * n              # 親 -1は根

# 隣接リストの作成
for i in range(m):
    # a->b 有向辺
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    in_cnt[b] += 1

q = deque([i for i in range(n) if in_cnt[i]==0])

while q:
    p = q.popleft()
    ts.append(p)
    for nxt in edges[p]:
        in_cnt[nxt] -= 1
        if in_cnt[nxt] == 0:
            q.append(nxt)
            parents[nxt] = p



print(ts)
print(parents)

### len(ts)==m だったら閉路なし