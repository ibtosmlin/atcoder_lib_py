n = 100000

##############################
# 素数列挙
##############################
primes = set(range(3, n+1, 2))|set([2])
for i in range(3, int(n**0.5+1)):
    primes.difference_update(range(i*3, n+1, i*2))
primes = list(primes)

##############################
# ある数で何回割れるか
##############################
def divind(n,p):
    ret = 0
    while n%p==0:
        n//=p
        ret+=1
    return ret

##############################
# 素因数分解
##############################
def factorization(n):
    primen, degree, primend = [], [], {}
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            primen.append(i)
            degree.append(cnt)
            primend[i] = cnt
    if temp!=1:
        primen.append(temp)
        degree.append(1)
        primend[temp] = 1
    if primen==[]:
        primen.append(n)
        degree.append(1)
        primend[n] = 1
    return primend
#    return primen,degree

ans = factorization(72)
print(ans)  # 72 = 2**5 * 3**4
print(ans[0])  # prime number
print(ans[1])  # degree

##############################
# 約数列挙 O(n**0.5)
##############################
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]