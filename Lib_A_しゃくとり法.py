####################
# しゃくとり法
####################
N, K = map(int, input().split())
A = list(map(int,input().split()))
cnt = 0
sum = 0
r = 0               #right
for l in range(0,N):#left
    while (sum < K):###############条件
        if r == N:
            break
        else:
            sum += A[r]
            r += 1
    if sum < K:####################条件
        break
    cnt += N-r+1
    sum -= A[l]
print(cnt)


####################
# しゃくとり
####################
n=10
a=[3,5,2,4,8,7,10,9,1,6]

count=0
right=0
m=dict()
for left in range(n):
    while right<n and m.get(a[right],0)==0:
        m[a[right]]=m.get(a[right],0)+1
        right+=1
    count=max(count,right-left)
    m[a[left]]=m.get(a[left],1)-1
print(count)
