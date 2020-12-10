#!/usr/bin python3
# -*- coding: utf-8 -*-

# 優先度付きキュー
# 優先度とフラグを入れ込んだキューで、優先度が高い（数が小さい）ものからポップできる
# 優先度が低いものとする場合は、マイナスでキューにプッシュする
# hp キュー
# hist フラグの履歴（一度読んだものは再度使わない場合）

from heapq import heapify, heappop, heappush
from heapq import heappushpop, heapreplace
# heappushpop プッシュしてから最小値を取り出す
# heapreplace 最小値を取り出してプッシュする

hp = []
heapify(hp)
heappush(hp, (1,'a'))
hist = {'a'}
while len(hp)>0:
#    for k in range(K):
    v, tp = heappop(hp)
    print(v, tp)
    if tp in hist: continue
    #次の情報 nv, ntp
    heappush(hp, (nv,ntp))
    hist.add(ntp)
