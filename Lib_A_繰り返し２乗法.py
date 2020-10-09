#!/usr/bin python3
# -*- coding: utf-8 -*-

# スカラー
def pow(x, n):
    ret = 1
    for _ in range(n):
        if n & 1:
            ret *= x
        x *= x
        n >>= 1
        if n == 0: break
    return ret

#!/usr/bin python3
# -*- coding: utf-8 -*-

# 行列

mod = 10**9+7

def prod(ma, mb):
    n = len(ma)
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j] += ma[i][k]*mb[k][j]
                ret[i][j] %= mod
    return ret

def powmat(ma, k):
    n = len(ma)
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        ret[i][i] = 1
    for _ in range(k):
        if k & 1:
            ret = prod(ret, ma)
        ma = prod(ma, ma)
        k >>= 1
        if k == 0: break
    return ret

n, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
print(sum(sum(x)%mod for x in powmat(A, k))%mod)