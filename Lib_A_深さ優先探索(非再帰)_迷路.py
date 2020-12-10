#!/usr/bin python3
# -*- coding: utf-8 -*-

from collections import deque

def dfs(init):
    next_q = deque([])
    for hi, wi in init:
        next_q.append([hi, wi])
        dist[hi][wi] = 0

    while len(next_q)!=0:
        #スタック取り出し
        h,w = next_q.pop()
        for d in direc:
            hs, ws = h + d[0], w + d[1]
            if not (0<=hs<h and 0<=ws<w): continue
            if gmap[hs][ws]=='#': continue
            if dist[hs][ws]!=INF: continue
            next_q.append([hs,ws])
            dist[hs][ws] = dist[h][w] + 1
    return dist

##################################################

h, w = map(int,input().split())
sth, stw = 0, 0
glh, glw = h-1, w-1
#sth,stw = list(map(int,input().split()))
#sth, stw = sth-1, stw-1
#glh, glw = list(map(int,input().split()))
#glh, glw = glh-1, glw-1

INF = -1
gmap = [list(input()) for _ in range(h)]
dist = [[INF]*w for _ in range(h)]
direc = {(1,0), (-1,0), (0,1), (0,-1)}
init_q =[None]

#固定
init_q.append([sth, stw])
#複数
for sth in range(h):
    for stw in range(w):
        if gmap[sth][stw]=='#':
            init_q.append([sth,stw])

ret = dfs(init_q)
print(dist[glh][glw])
