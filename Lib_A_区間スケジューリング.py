#!/usr/bin python3
# -*- coding: utf-8 -*-

# 区間スケジューリング問題
# 区間の集合の中から、重ならないように最大で何個選べるか.
# 区間を「終端が早い順」にソートして、とれる順にとる Greedy で解く.
# XL<-区間の集合

def main():
    N = int(input())
    XL = [None] * N
    for n in range(N):
        X, L = map(int,input().split())
        XL[n] = (X-L,X+L)
    XL.sort(key=lambda x:x[1])
    ret = 0
    TMP = XL[0][0]
    for x in XL:
        if TMP <= x[0]:
            TMP = x[1]
            ret += 1
    print(ret)

if __name__ == '__main__':
    main()