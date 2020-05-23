#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    XL = [None] * N
    for n in range(N):
        X, L = map(int,input().split())
        XL[n] = [X-L,X+L]
    XL.sort(key=lambda x:x[1])
    ret = 1
    TMP = XL[0][1]
    for x in XL[1:]:
        if TMP<=x[0]:
            TMP = x[1]
            ret += 1
    print(ret)

if __name__ == '__main__':
    main()