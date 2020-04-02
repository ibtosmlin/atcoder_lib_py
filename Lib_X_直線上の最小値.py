def dist(p,A):        #効用関数
  r = 0
  for x in A:
    r += (x-p)*(x-p)  #距離
  return r

N = int(input())
A = list(map(int,input().split()))
f,t = min(A),max(A)

ret=1001001001
for p in list(range(f,t+1)):
  ret = min(ret, dist(p,A))  
print(ret)