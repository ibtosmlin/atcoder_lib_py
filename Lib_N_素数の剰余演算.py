#####################################積
def prod_mod(x, mod):
    ans = 1
    for i in x:
        ans = ( ans * ( i % mod ) ) % mod
    return ans

A = [111111111,123456789,987654321]
B = [111111111,123456789,-987654321]
print(prod_mod(A,10**9+7))
print(prod_mod(B,10**9+7))

#####################################和
def plus_mod(x, mod):
    ans = 0
    for i in x:
        ans = ( ans + ( i % mod ) ) % mod
    return ans

A = [111111111,123456789,987654321]
B = [111111111,123456789,-987654321]
print(plus_mod(A,10**9+7))
print(plus_mod(B,10**9+7))

#####################################素数の累乗
def pow_mod(x,n,mod):
    ans = 1
    xx = x % mod
    bin_n = format(n, 'b')
    print(bin_n)
    K = len(bin_n)
    xn = [x % mod]
    for i in range(1,K):
        xn.insert(0, (xn[0] ** 2) % mod )
    for i in range(K):
        if int(bin_n[i])==1:
            ans = ( ans * xn[i] ) % mod
    return ans

def inv_mod(x, mod):
    return pow_mod(x,mod-2,mod)

#####################################x**n
def pow_mod(x,n,mod):
    ans = 1
    xx = x % mod
    bin_n = format(n, 'b')
    print(bin_n)
    K = len(bin_n)
    xn = [x % mod]
    for i in range(1,K):
        xn.insert(0, (xn[0] ** 2) % mod )
    for i in range(K):
        if int(bin_n[i])==1:
        ans = ( ans * xn[i] ) % mod
    return ans

print(pow_mod(7,8,13))
