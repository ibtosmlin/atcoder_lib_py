#!/usr/bin python3
# -*- coding: utf-8 -*-

#######################################################################
# ナップサック
# 重さ：Wー10**5くらい
# 価値：N*max_Viー10**11くらい
# dp[w]:wの重さで可能な最大の価値
#   dp[w]とdp[w-wi]+vi(i番目のアイテムをとる場合)　との大きいほうで更新
#######################################################################

import numpy as np

def main():
    N, W = map(int, input().split())
    dp = [0] * (W+1)
    dp = np.array(dp)
    for _ in range(N):
        w_, v_ = map(int, input().split())
        dp[w_:] = np.maximum(dp[w_:], dp[:-w_] + v_)
#    print(dp)
    print(dp[W])

if __name__ == '__main__':
    main()