#!/usr/bin python3
# -*- coding: utf-8 -*-

from collections import deque

H, W = map(int,input().split())
sth, stw = 0, 0
glh, glw = H-1, W-1
#sth,stw = list(map(int,input().split()))
#sth, stw = sth-1, stw-1
#glh, glw = list(map(int,input().split()))
#glh, glw = glh-1, glw-1

INF = -1
Gmap = [list(input()) for _ in range(H)]
Dist = [[INF]*W for _ in range(H)]
direc = {(1,0), (-1,0), (0,1), (0,-1)}
next_q = deque([])

def bfs_settings():
    #固定
    next_q.append([sth, stw])
    Dist[sth][stw]=0

    #複数
    for h in range(H):
        for w in range(W):
            if Gmap[h][w]=='#':
                next_q.append([h,w])
                dist[h][w]=0

def bfs():
    ret = True
    while len(next_q)!=0:
        #キュー取り出し(先頭)
        h,w = next_q.popleft()
        for d in direc:
            hs, ws = h + d[0], w + d[1]
            if not (0<=hs<H and 0<=ws<W):
                continue
            if Gmap[hs][ws]=='.' and Dist[hs][ws]==INF:
                next_q.append([hs,ws])
                Dist[hs][ws] = Dist[h][w] + 1
    return ret

def main():
    bfs_settings()
    ret = bfs()
    print(Dist[glh][glw])

if __name__ == '__main__':
    main()