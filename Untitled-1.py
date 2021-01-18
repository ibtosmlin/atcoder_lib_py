# Reference: https://qiita.com/dn6049949/items/afa12d5d079f518de368
# self.data: 1-indexed
#    __1__
#  _2_   _3_
# 4   5 6   7
# f(f(a, b), c) == f(a, f(b, c))

class SegmentTree:
    # a = [default] * n
    def __init__(self, n, f=max, default=-10**18):
        self.num_leaf = 1
        while self.num_leaf < n:
            self.num_leaf *= 2
        self.data = [default] * (2*self.num_leaf)
        self.f = f

    # a[i] = x
    def update(self, i, x):
        i += self.num_leaf
        self.data[i] = x
        i >>= 1
        while i > 0:
            self.data[i] = self.f(self.data[2*i], self.data[2*i+1])
            i >>= 1

    # return f(a[l:r])
    def query(self, l, r):
        l += self.num_leaf
        r += self.num_leaf - 1
        lres, rres = self.data[0], self.data[0] # self.data[0] == default
        while l < r:
            if l & 1: # l % 2 == 1
                lres = self.f(lres, self.data[l])
                l += 1
            if not r & 1: # r % 2 == 0
                rres = self.f(self.data[r], rres)
                r -= 1
            l >>= 1 # l //= 2
            r >>= 1 # r //= 2
        if l == r:
            res = self.f(self.f(lres, self.data[l]), rres)
        else:
            res = self.f(lres, rres)
        return res

    # You can use lower_bound only if f == max.
    # return min({i | x <= i and v <= a[i]}, self.num_leaf)
    def lower_bound(self, x, v):
        x += self.num_leaf
        while self.data[x] < v:
            if x & 1: # x % 2 == 1
                if len(bin(x)) == len(bin(x+1)):
                    x += 1
                else:
                    return self.num_leaf
            else:
                x >>= 1
        while x < self.num_leaf:
            if self.data[2*x] >= v:
                x = 2*x
            else:
                x = 2*x + 1
        return x - self.num_leaf

def main():
    from sys import stdin
    input = stdin.buffer.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    st = SegmentTree(n=n, f=max, default=-1)
    for i, ai in enumerate(a):
        st.update(i, ai)

    ans = []
    for _ in range(q):
        t, x, v = map(int, input().split())
        if t == 1:
            st.update(x-1, v)
        elif t == 2:
            ans.append(st.query(x-1, v))
        else:
            ans.append(min(st.lower_bound(x-1, v), n) + 1)

    for i in ans:
        print(i)

main()