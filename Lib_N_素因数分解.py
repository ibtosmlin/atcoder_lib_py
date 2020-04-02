def factorization(n):
  primen = []
  degree = []
  primend = []
  temp = n
  for i in range(2, int(-(-n**0.5//1))+1):
    if temp%i==0:
      cnt=0
      while temp%i==0:
        cnt+=1
        temp //= i
      primen.append(i)
      degree.append(cnt)
      primend.append([i,cnt])
  if temp!=1:
    primen.append(temp)
    degree.append(1)
    primend.append([temp,1])
  if primen==[]:
    primen.append(n)
    degree.append(1)
    primend.append([n,1])
  return primen,degree
ans = factorization(2592)
print(ans)  # 72 = 2**5 * 3**4
print(ans[0])  # prime number
print(ans[1])  # degree

############
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors