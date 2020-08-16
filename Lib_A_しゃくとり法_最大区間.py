#!/usr/bin python3
# -*- coding: utf-8 -*-

############################################
# しゃくとり法
############################################
# 区間において掛け算がK以下となる最大区間の長さ ABC032_C
############################################

N = int(input())
N, K = map(int, input().split())
A = list(map(int, input().split()))
A = list(int(input()) for _ in range(N))
##
#    N = 7
#    K = 6
#    A = [4,3,1,1,2,10,2]
#    answer = 4
##
if 0 in A:
    ret = N
else:
    ret = 0
    right = 0
    seki = 1
    for left in range(0,N):
        while (right < N and seki * A[right] <= K):   #####条件
            seki *= A[right]
            right += 1
        ret = max(ret, right-left)              #####値の更新
#            print(ret, left, right)
        if left == right:
            right += 1
        else:
            seki //= A[left]                     #####left分除く

print(ret)
