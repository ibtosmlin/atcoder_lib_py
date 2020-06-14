########################################
# ナップサック
# max_Wi,Wー10**5くらい
# N*max_Viー10**11くらい
# dp[w]:wの重さで可能な最大の価値
########################################

import sys
input = sys.stdin.readline
import numpy as np
N,W=map(int, input().split())
dp = np.zeros(W+1, dtype=np.int)
for i in range(N):
  wi,vi=map(int,input().split())
  dp[wi:]=np.maximum(dp[wi:], dp[:-wi]+vi)
print(dp[W])



########################################
# ナップサック
# max_Wi,Wー10**9くらい
# N*max_Viー10**5くらい
# dp[v]:v以上の価値となる最小の重さ
########################################

import sys
input = sys.stdin.readline
import numpy as np
N,W=map(int,input().split())
max_V = N*(10**3)
max_Wi = W
dp=np.array([0]+[max_Wi+1]*(max_V))
for i in range(N):
  wi,vi=map(int,input().split())
  dp[vi:]=np.minimum(dp[vi:],dp[:-vi]+wi)
print(np.max(np.where(dp <= W)))
