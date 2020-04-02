##############################
# 偶数・奇数
##############################
N = 100
odd  = [2*i for i in range(N//2+1)]
even = [2*i+1 for i in range((N-1)//2+1)]

##############################
# 素数列挙
##############################
n = 100000
primes = set(range(3, n+1, 2))|set([2])
for i in range(3, int(n**0.5+1)):
    primes.difference_update(range(i*3, n+1, i*2))
primes = list(primes)

##############################
# alphabet 
# 'abcdefghijklmnopqrstuvwxyz'
##############################
al = 'abcdefghijklmnopqrstuvwxyz'
AL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

al = [chr(ord('a') + i) for i in range(26)]

ord('a') #chr->ascii
chr(413) #ascii->chr