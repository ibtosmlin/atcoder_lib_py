##############################
# 迷路BFS
##############################
from collections import deque
H,W = map(int,input().split())
Gd = [list(input()) for _ in range(H)]
ans = 0
for i in range(H):
  ans += Gd[i].count('.')
INF = -1
def dfs(start,goal):
    q = deque([])# スタック
    Dis[start[0]][start[1]]=1
    q.append(start)
    while len(q)!=0:
        h,w = q.popleft()# スタック取りだし（先頭）
        for d in direc:
            hs, ws = h + d[0], w + d[1]
            if not (0<=hs<H and 0<=ws<W):
            continue
            if Gd[hs][ws]=='.' and Dis[hs][ws]==INF:
                q.append([hs,ws])
                Dis[hs][ws]=Dis[h][w]+1
    return Dis[goal[0]][goal[1]]
minpath = dfs([0,0],[H-1,W-1])
if minpath = INF:
    ans = INF
else:
    ans = ans - minpath
print(ans)

##############################
# 迷路BFS
##############################
from collections import deque
H,W = map(int,input().split())
Gd = [list(input()) for _ in range(H)]
INF = -1
direc = [[1,0],[-1,0],[0,1],[0,-1]]
def dfs(start):
    Dis = [[INF]*W for _ in range(H)]
    Dis[start[0]][start[1]]=0
    q = deque([])# スタック
    q.append(start)
    r = 0
    while len(q)!=0:
        h,w = q.popleft()# スタック取りだし（先頭）
    
        for d in direc:
            hs, ws = h + d[0], w + d[1]
            if not (0<=hs<H and 0<=ws<W):
                continue
            if Gd[hs][ws]=='.' and Dis[hs][ws]==INF:
                q.append([hs,ws])
                Dis[hs][ws] = Dis[h][w] + 1
                r = max(Dis[hs][ws],r)
    return r
ans = INF
for h in range(H):
    for w in range(W):
        if Gd[h][w]=='.':
            ans = max(ans,dfs([h,w]))
print(ans)