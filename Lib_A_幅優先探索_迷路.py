#!/usr/bin python3
# -*- coding: utf-8 -*-

from collections import deque

H, W = map(int,input().split())
sth, stw = 0, 0
glh, glw = H-1, W-1
INF = -1
gmap = [list(input()) for _ in range(H)]
dist = [[INF]*W for _ in range(H)]
direc = {(1,0), (-1,0), (0,1), (0,-1)}

def find_start_goal(gmap):
    for h in range(H):
        for w in range(W):
            if gmap[h][w]=='s':
                sth, stw = h, w
            elif gmap[h][w]=='g':
                glh, glw = h, w
    return [sth, stw], [glh, glw]

def bfs(init):
    next_q = deque([])
    for i in init:
        h, w = i
        next_q.append(i)
        dist[h][w] = 0

    while len(next_q)!=0:
        #キュー取り出し(先頭)
        h,w = next_q.popleft()
        for dh, dw in direc:
            hs, ws = h + dh, w + dw
            if not (0<=hs<H and 0<=ws<W): continue
            if gmap[hs][ws]=='.' and dist[hs][ws]==INF:
                next_q.append([hs,ws])
                dist[hs][ws] = dist[h][w] + 1
    return dist

init_q =[]
init_q.append([sth, stw])
ret = bfs(init_q)
print(ret[glh][glw])
