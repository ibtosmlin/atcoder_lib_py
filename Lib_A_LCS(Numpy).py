#!/usr/bin python3
# -*- coding: utf-8 -*-

####################################################
# LCS(longest common sequence)
# 部分列で最長の共通のもの
####################################################

# dp[i+1][j+1]:= s の i 文字目までと t の j 文字目まででの LCS の長さ

import numpy as np

def main():
    S = np.array(list(input()), dtype='unicode')
    T = np.array(list(input()), dtype='unicode')
    ls = len(S)
    lt = len(T)

    equal = S[:, None] == T[None,:]
#    print(eq)
    dp = np.zeros((ls + 1, lt + 1), dtype=int)

    for i in range(ls):
        dp[i + 1][1:] = np.maximum(dp[i][1:], dp[i][:-1] + equal[i])
        dp[i + 1] = np.maximum.accumulate(dp[i + 1])
#    for i in range(ls):
#        for j in range(lt):
#            dp[i+1][j+1] = max(dp[i][j+1], dp[i][j]+ eq[i][j])
#            dp[i+1][j+1] = max(dp[i+1][j+1] , dp[i+1][j])
#    print(dp)

    # 復元
    res = ''
    i, j = ls, lt
    while (i > 0 and j > 0):
        # (i-1, j) -> (i, j) と更新されていた場合
        if dp[i][j] == dp[i-1][j]:
            i-=1   # DP の遷移を遡る
        # (i, j-1) -> (i, j) と更新されていた場合
        elif dp[i][j] == dp[i][j-1]:
            j-=1   # DP の遷移を遡る
        # (i-1, j-1) -> (i, j) と更新されていた場合
        else:
            res += S[i-1]
            # このとき s[i-1] == t[j-1] なので、t[j-1] + res でも OK
            i-=1
            j-=1   # DP の遷移を遡る
    print(res[::-1])

if __name__ == '__main__':
    main()