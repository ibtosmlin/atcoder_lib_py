#!/usr/bin python3
# -*- coding: utf-8 -*-

#######################################################################
# ナップサック
# 重さ：max_wi,Wー10**9くらい
# 価値：N*max_viー10**5くらい
# dp[v]:v以上の価値となる最小の重さ
#   dp[v]とdp[v-vi]+wi(i番目のアイテムをとる場合)　との小さいほうで更新
#######################################################################

import numpy as np

N, W = map(int, input().split())
max_vi = 10**3
max_V = N*max_vi
dp = [W+1] * (max_V+1)
dp[0] = 0
dp = np.array(dp)
for _ in range(N):
    w_, v_ = map(int, input().split())
    dp[v_:] = np.minimum(dp[v_:], dp[:-v_] + w_)
#    print(dp)
print(np.max(np.where(dp <= W)))
