##############################
# priority que
##############################
X,Y,Z,K = map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

def Nmb(tp):
    return A[tp[0]-1]+B[tp[1]-1]+C[tp[2]-1]

from heapq import heapify, heappop, heappush, heappushpop
hp = []
heapify(hp)
tp = (1, 1 , 1)
heappush(hp, (-Nmb(tp),)+tp)
hist = {tp}

for k in range(K):
#最上位をpop
    rec = heappop(hp)
    print(rec[0]*-1)
# 次の順位を登録する
# Aを次の配列
    tp = (rec[1]+1, rec[2], rec[3])
    if tp[0]<=X and not tp in hist:
        heappush(hp, (-Nmb(tp),)+tp)
        hist.add(tp)
# Bを次の配列
    tp = (rec[1], rec[2]+1, rec[3])
    if tp[1]<=Y and not tp in hist:
        heappush(hp, (-Nmb(tp),)+tp)
        hist.add(tp)
# Cを次の配列
    tp = (rec[1], rec[2], rec[3]+1)
    if tp[2]<=Z and not tp in hist:
        heappush(hp, (-Nmb(tp),)+tp)
        hist.add(tp)