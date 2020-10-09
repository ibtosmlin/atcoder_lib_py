#!/usr/bin python3
# -*- coding: utf-8 -*-

# 転倒数
# 配列中 i<j, ai>ajとなるものの個数
# https://atcoder.jp/contests/chokudai_S001/tasks/chokudai_S001_j

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

n = int(input())
a = list(map(int, input().split()))
n = max(a)+2

bit = BinaryIndexedTree(n)

ret = 0
for i, ai in enumerate(a):
    ret += i - bit.sum(ai)
    bit.add(ai, 1)
print(ret)
