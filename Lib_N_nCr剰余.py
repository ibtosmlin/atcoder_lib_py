#####################################
# nCr % 10**9+7
#####################################
mod = 10**9+7               # mod素数
N = 10**5                   # 出力の制限
g1 = [1]*(N+1)              # 元テーブル
g2 = [1]*(N+1)              # 逆元テーブル
for i in range( 2, N + 1 ): # 準備
    g1[i] = ( g1[i-1] * i ) % mod
    g2[i] = ( g2[i-1] * pow(i,mod-2,mod) ) % mod

def nCr(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

ret = nCr(4, 2, mod)

#####################################
# nCr % 10**9+7  n～10^9　r～10^5
# nは大きいが　rは小さい場合
#####################################
mod = 10 ** 9 + 7   # mod素数
n,r = 4,3           # 出力の制限
def nCr(n, r, mod):
    ret = [1]*(r+1)
    for i in range(1, r+1):
        ret[i] = (ret[i-1] * (n-i+1) * pow(i,mod-2,mod)) % mod
    return ret
nCrl = nCr(n, r, mod)
print(nCrl[1:])     #[4,6,4]配列として出力