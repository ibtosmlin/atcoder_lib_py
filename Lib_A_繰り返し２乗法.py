# スカラー
def pow(x, n):
    ret = 1
    while n>0:
        if n & 1:
            ret *= x
        x *= x
        n >>= 1
    return ret

# 行列
import numpy as np

A = [[0,1],[1,1]]
matA = np.matrix(A, dtype=np.int64)
def pow_matrix(matA, n):
    ret = 1
    while n>0:
        if n & 1:
            ret *= matA
        matA *= matA
        n >>= 1
    return ret
