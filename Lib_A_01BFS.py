#!/usr/bin python3
# -*- coding: utf-8 -*-

# https://atcoder.jp/contests/abc176/tasks/abc176_d

########################################################
# 01BFS
########################################################

from collections import deque

h, w = map(int, input().split())
sh, sw = map(int, input().split())
gh, gw = map(int, input().split())
sh, sw, gh, gw = sh-1, sw-1, gh-1, gw-1
gmap = [input() for _ in range(h)]
direc = {(1, 0), (-1, 0), (0, 1), (0, -1)}  # {(1, 1), (1, -1), (-1, 1), (-1, -1)}
direcwp = {(i, j) for i in range(-2, 3) for j in range(-2, 3)} - {(0, 0)}
direcwp = direcwp - direc
INF = float('inf')
dist = [[INF] * w for _ in range(h)]

def zero_one_bfs(sh, sw, gh, gw):
    next_q = deque([])
    next_q.append((sh, sw))
    dist[sh][sw] = 0
    while next_q:
        ch, cw = next_q.popleft()
        cd = dist[ch][cw]
        if ch == gh and cw == gw: return cd
        for dh, dw in direc:
            nh, nw = ch+dh, cw+dw
            if not (0<=nh<h and 0<=nw<w): continue
            if gmap[nh][nw] == '#': continue
            if dist[nh][nw] <= cd: continue
            dist[nh][nw] = cd
            next_q.appendleft((nh, nw))
        for dh, dw in direcwp:
            nh, nw = ch+dh, cw+dw
            if not (0<=nh<h and 0<=nw<w): continue
            if gmap[nh][nw] == '#': continue
            if dist[nh][nw] <= cd+1: continue
            dist[nh][nw] = cd+1
            next_q.append((nh, nw))
    return dist[gh][gw]

ret = zero_one_bfs(sh, sw, gh, gw)
print(-1 if ret == INF else ret)


#!/usr/bin python3
# -*- coding: utf-8 -*-

########################################################
# 0123...BFS 01の他いくつかの値を持つ場合
########################################################

from collections import deque

h, w = map(int, input().split())
sh, sw = map(int, input().split())
gh, gw = map(int, input().split())
sh, sw, gh, gw = sh-1, sw-1, gh-1, gw-1
gmap = [input() for _ in range(h)]
direc0 = {(1, 0), (-1, 0), (0, 1), (0, -1)}  # {(1, 1), (1, -1), (-1, 1), (-1, -1)}
direc1 = {(i, j) for i in range(-2, 3) for j in range(-2, 3)} - {(0, 0)}
direc1 = direc1 - direc0
INF = float('inf')
dist = [[INF] * w for _ in range(h)]

def bfs(sh, sw, gh, gw):
    next_q0 = deque([])
    next_q1 = deque([])
    next_q0.append((sh, sw))
    dist[sh][sw] = 0
    while next_q0 or next_q1:
        while next_q0:
            ch, cw = next_q0.popleft()
            cd = dist[ch][cw]
            if ch == gh and cw == gw: return cd
            next_q1.append((ch, cw))
            for dh, dw in direc0:
                nh, nw = ch+dh, cw+dw
                if not (0<=nh<h and 0<=nw<w): continue
                if gmap[nh][nw] == '#': continue
                if dist[nh][nw] <= cd: continue
                dist[nh][nw] = cd
                next_q0.append((nh, nw))
        while next_q1:
            ch, cw = next_q1.popleft()
            cd = dist[ch][cw]
            for dh, dw in direc1:
                nh, nw = ch+dh, cw+dw
                if not (0<=nh<h and 0<=nw<w): continue
                if gmap[nh][nw] == '#': continue
                if dist[nh][nw] <= cd+1: continue
                dist[nh][nw] = cd+1
                next_q0.append((nh, nw))
    return dist[gh][gw]

ret = bfs(sh, sw, gh, gw)
print(-1 if ret == INF else ret)


#!/usr/bin python3
# -*- coding: utf-8 -*-

########################################################
# ダイクストラを使う方法
########################################################

from heapq import heapify, heappop, heappush

h, w = map(int, input().split())
sh, sw = map(int, input().split())
gh, gw = map(int, input().split())
sh, sw, gh, gw = sh-1, sw-1, gh-1, gw-1
gmap = [input() for _ in range(h)]
direc = {(1, 0), (-1, 0), (0, 1), (0, -1)}  # {(1, 1), (1, -1), (-1, 1), (-1, -1)}
direcwp = {(i, j) for i in range(-2, 3) for j in range(-2, 3)} - {(0, 0)}
direcwp = direcwp - direc
INF = float('inf')
dist = [[INF] * w for _ in range(h)]

def zero_one_bfs(sh, sw, gh, gw):
    next_q = []
    heapify(next_q)
    dist[sh][sw] = 0
    heappush(next_q, (0, sh, sw))
    while next_q:
        cd, ch, cw = heappop(next_q)
        if ch == gh and cw == gw: return cd
        for dh, dw in direc:
            nh, nw = ch+dh, cw+dw
            if not (0<=nh<h and 0<=nw<w): continue
            if gmap[nh][nw] == '#': continue
            if dist[nh][nw] <= cd: continue
            dist[nh][nw] = cd
            heappush(next_q, (cd, nh, nw))
        for dh, dw in direcwp:
            nh, nw = ch+dh, cw+dw
            if not (0<=nh<h and 0<=nw<w): continue
            if gmap[nh][nw] == '#': continue
            if dist[nh][nw] <= cd+1: continue
            dist[nh][nw] = cd+1
            heappush(next_q, (cd+1, nh, nw))
    return dist[gh][gw]

ret = zero_one_bfs(sh, sw, gh, gw)
print(-1 if ret == INF else ret)
