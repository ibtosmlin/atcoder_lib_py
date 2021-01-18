#!/usr/bin python3
# -*- coding: utf-8 -*-

# topological sort 数え上げ
# https://atcoder.jp/contests/abc041/tasks/abc041_d/

n, m = map(int, input().split())
edges = [0]*n

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a] += 1 << b

dp = [0] * (1 << n)
dp[0] = 1

# ノードIDと対応するビット位置は繰り返し求めるので事前計算しておく
jbs = [(j, 1 << j) for j in range(n)]

for ib in range(1 << n):# 過去の訪問済み状態
    for j, jb in jbs:   # 次の行先
        if ib & jb: continue        # ib状態にjbが入っている過去に訪問済み×
        if ib & edges[j]: continue  # jの次に行った先が訪問済み箇所だと×
        dp[i | jb] += dp[i]

print(dp[-1])