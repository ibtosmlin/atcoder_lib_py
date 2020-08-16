#!/usr/bin python3
# -*- coding: utf-8 -*-

h, w = list(map(int, input().split()))
gd = [[0]*(w+1)]
for _ in range(h):
    gd.append([0] + list(map(int,input().split())))

for i in range(1, h+1):
    for j in range(1, w+1):
        gd[i][j] += gd[i][j-1]
for j in range(1, w+1):
    for i in range(1, h+1):
        gd[i][j] += gd[i-1][j]

def cnt(x, y, u, v):
    return gd[u][v]-gd[u][y]-gd[x][v]+gd[x][y]
