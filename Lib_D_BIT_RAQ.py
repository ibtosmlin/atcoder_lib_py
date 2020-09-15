#!/usr/bin python3
# -*- coding: utf-8 -*-

# Binary Indexed Tree for Range Add Query
# 1-indexed
#    初期値は a_1 = a_2 = ... = a_n = 0
#    ・add(l,r,x): [l,r) に x を加算する
#    ・sum(i): a_1 + a_2 + ... + a_i を計算する

class BinaryIndexedTree:
    # 初期化処理
    def __init__(self, size):
        self.size = size
        self.dat = [0]*(size+1)
        self.depth = size.bit_length()

    def init(self, a):
        for i, x in enumerate(a):
            self.add(i, x)

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

# sum(i) >= vとなる最小のindex
    def lower_bound(self, x):
        """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.dat[k] < x:
                sum_ += self.dat[k]
                pos += 1 << i
        return pos  #0-indexed

#### for debug
    def get_original_sequence(self):
        ret = self.get_aggrigate_sequence()
        for i in range(self.size-1, 0, -1):
            ret[i] -= ret[i-1]
        return ret

    def get_aggrigate_sequence(self):
        return [bit.sum(i) for i in range(self.size)]

    def __str__(self):
        seq = self.get_original_sequence()
        ret = 'original :' + ' '.join(map(str, seq))
        ret += '\n'
        seq = self.get_aggrigate_sequence()
        ret += 'aggrigate:' + ' '.join(map(str, seq))
        return ret

class BitRAQ:
    def __init__(self, size):
        self.size = size
        self.bit0 = BinaryIndexedTree(size)
        self.bit1 = BinaryIndexedTree(size)

    def init(self, a):
        self.bit0.init(a)

    def add(self, l, r, x):
        self.bit0.add(l, -x * (l - 1))
        self.bit0.add(r, x * (r - 1))
        self.bit1.add(l, x)
        self.bit1.add(r, -x)

    def sum(self, r):
        return self.bit0.sum(r) + self.bit1.sum(r) * r
##################################
#n = int(input())
#a = list(map(int, input().split()))
a = [5,3,7,9,6,4]
n = len(a)

bit = BitRAQ(n)
bit.init(a)
bit.add(2,4,5)
for i in range(n):
    print(bit.sum(i))
