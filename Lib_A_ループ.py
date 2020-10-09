#!/usr/bin python3
# -*- coding: utf-8 -*-

# ループを検索して計算量圧縮
# 0->1->...->st->st+1->...->st+lp-1-┐
#             └─────────────────────┘
#                       lp

n, k = map(int, input().split())
a = list(map(int, input().split()))

nth = k     #取得位置
x = a[0]    #初期値
def next(x):#ネクスト関数
    ret = a[x-1]
    return ret

seen = set([])
seqs = []
for i in range(n+1):
    seen.add(x)
    seqs.append(x)
    x = next(x)
    if x in seen: break
start = seqs.index(x)
lp = len(seqs) - start

lpsum = sum(seqs[start:])
lptimes = (nth-(start+lp)+(lp-1))//lp
ret_sum = lpsum * lptimes
nth -= lp * lptimes
ret_sum += sum(seqs[:nth])
ret_val = seqs[nth-1]

#print(ret_sum)
print(ret_val)
