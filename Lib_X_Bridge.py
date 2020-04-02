N, M = map(int, input().split())
d=[[] for i in range(N)]
for i in range(M):
    b, c = map(int, input().split())
    d[b-1].append(c-1)
    d[c-1].append(b-1)
a=0
while True:
    count = 0
    for i in range(N):
        if len(d[i]) == 1:
            d[d[i][0]].remove(i)
            d[i]=[]
            count += 1
    if count == 0:
        break
    a+=count
print(a)
