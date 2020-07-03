#!/usr/bin python3
# -*- coding: utf-8 -*-

############################################
# しゃくとり法
############################################
# 区間において単調増加となるものの個数　ABC038_c
############################################

def main():
    N = int(input())
    A = list(map(int, input().split()))
##
    ret = 0
    right = 0
#    conditon = 999
    for left in range(0,N):
        if right < N and left == right:
            right += 1
        while (right < N and A[right-1] < A[right]):   #####条件
#    conditon = 999
            right += 1
        ret += right - left                  #####値の更新
#        print("A", ret, left, right)

    print(ret)

if __name__ == '__main__':
    main()