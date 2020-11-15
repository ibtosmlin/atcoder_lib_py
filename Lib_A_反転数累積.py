#!/usr/bin python3
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/past202010-open/tasks/past202010_k

class BinaryIndexedTree:
    # 初期化処理
    def __init__(self, size):
        self.size = size
        self.dat = [0]*(size+1)
        self.depth = size.bit_length()

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.dat[i] += x
            i += i & -i # 更新すべき位置

    def sum(self, r):
        r += 1
        ret = 0
        while r>0:
            ret += self.dat[r]
            r -= r & -r # 加算すべき位置
        return ret

    def get_original_sequence(self):
        ret = self.get_aggrigate_sequence()
        for i in range(self.size-1, 0, -1):
            ret[i] -= ret[i-1]
        return ret

    def get_aggrigate_sequence(self):
        return [self.sum(i) for i in range(self.size)]

mod = 10**9
k = int(input())
a = []
for i in range(k):
    n = int(input())
    a.append(list(map(int, input().split())))

q = int(input())
b = list(map(int, input().split()))

seen = [False] * k
t_a = [0] * k
c_a = [[0]*21 for _ in range(k)]
sum_c_a = [[0]*21 for _ in range(k)]

ret = 0
sum_c = [0] * 21
for bi in b:
    bi -= 1
    if seen[bi] == False:
        bit = BinaryIndexedTree(21)
        tnt = 0
        for i, xi in enumerate(a[bi]):
            tnt += i - bit.sum(xi)
            tnt %= mod
            bit.add(xi, 1)
        t_a[bi] = tnt%mod
        c_a[bi] = bit.get_original_sequence()
        sum_c_a[bi] = bit.get_aggrigate_sequence()
        seen[bi] = True
    t = t_a[bi]
    c = c_a[bi]
    sc = sum_c_a[bi]
    # 追加区間分
    ret += t
    # 元の区間>追加区間
    for i in range(1, 21):  # 追加区間がiの場合
        ret += c[i]*(sum_c[-1]-sum_c[i])
    #sum_cの更新
    for i in range(1, 21):
        sum_c[i] += sc[i]
    ret %= mod
print(ret)