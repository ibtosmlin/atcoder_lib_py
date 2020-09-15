#!/usr/bin python3
# -*- coding: utf-8 -*-
# 桁DP


# 1以上n以下の整数であって、 10進法で表したときに、0でない数字がちょうど
# k個あるようなものの個数
# https://atcoder.jp/contests/abc154/tasks/abc154_e

sn = input()
k = int(input())
l = len(sn)
#dp[i][j][status]   status=0 は小さいのが未確定=i文字まで同じ
#                   status=1 は小さいことが確定
# i桁目まで決めて、0でない桁がj個
# 初期値は1 からスタート s=0,i=0,j=0
dp = [[[0]*2 for j in range(k+1)] for i in range(l+1)]
dp[0][0][0] = 1
for i in range(l):
    ni = int(sn[i])
    for j in range(k+1):
        for st in range(2):
            for x in range(10):
                i_ = i+1
                j_ = j
                st_ = st
                if x != 0:
                    j_ += 1
                if j_ > k:
                    continue
                if st_ == 0 and x > ni:
                    continue
                if st_ == 0 and x < ni:
                    st_ = 1
                dp[i_][j_][st_] += dp[i][j][st]

print(sum(dp[l][k]))

#################################################################
#################################################################
#################################################################

#!/usr/bin python3
# -*- coding: utf-8 -*-

# https://atcoder.jp/contests/abc007/tasks/abc007_4
#
# 区間[A, B]={A, A+1, A+2, ..., B}の数うち、
# 10進表現で、4 と 9 が入っているようなものの個数

def cnt(n):
    sn = str(n)
    l = len(sn)
    #dp[i][status]   status=0 は小さいのが未確定=i文字まで同じ
    #                status=1 は小さいことが確定
    #i桁目まで決めて、4,9を含まない数の個数
    #初期値は1 からスタート s=0,i=0
    dp = [[0]*2 for i in range(l+1)]
    dp[0][0] = 1
    for i in range(l):
        ni = int(sn[i])
#       dp[i][1]    #4,9以外0,1,2,3,,5,6,7,8なら、なんでもOK 8通り
        dp[i+1][1] += dp[i][1] * 8
#       dp[i][0]    #niを選ぶ場合と、n未満を選ぶ場合
        dp[i+1][0] += dp[i][0] * (ni!=4) * (ni!=9)    #niを選ぶ>status=0
        dp[i+1][1] += dp[i][0] * ( ni - (ni>4) )      #0～(ni-1)を選ぶ>status=1
    return n - sum(dp[l])

a, b = map(int,input().split())
print(cnt(b)-cnt(a-1))
