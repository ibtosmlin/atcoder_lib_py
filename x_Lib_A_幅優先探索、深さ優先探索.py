################################################
# BFS 幅優先探索
################################################
from collections import deque
 
def bfs(path):
    q = deque([])   # キュー
    q.append(path)
    
    while len(q) > 0:
        p = q.popleft()     # キュー取りだし（先頭）
        print p
        for child in os.listdir(p):
            child_path = p + '/' + child
            if os.path.isdir(child_path):
                q.append(child_path)    # キュー追加
 
 
bfs('/root')

################################################
# DFS 深さ優先探索
################################################
from collections import deque
 
def dfs(path):
    q = deque([])   # スタック
    q.append(path)
    
    while len(q) > 0:
        p = q.pop()         # スタック取りだし（末尾）
        print p
        for child in os.listdir(p):
            child_path = p + '/' + child
            if os.path.isdir(child_path):
                q.append(child_path)   # スタック追加
 
 
dfs('/root')

X=int(input())

################################################
# BFS
################################################
from collections import deque
def bfs(start,goal):
    q = deque([])   # スタック
    q.append([start])
    flg = 0
    while flg==0:
        p = q.popleft()         # スタック取りだし（先頭）
        jp = len(p)
        if p[-1]-jp == goal or p[-1]+jp == goal:
            return jp
        else:
            p0 = [p[-1]]
            pp = [p[-1]+jp]
            pm = [p[-1]-jp]
            q.append(p+pp)# スタック追加
            q.append(p+pm)
        q.append(p+p0)

print(bfs(0,X))