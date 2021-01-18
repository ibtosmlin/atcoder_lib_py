# Reference: https://atcoder.jp/contests/practice2/submissions/17054293

class LazySegmentTree:
  def __init__(self, n, op, e, mapping, composition, id):
    self.n = n
    self.op = op
    self.e = e
    self.mapping = mapping
    self.composition = composition
    self.id = id
    self.log = (n - 1).bit_length()
    self.size = 1 << self.log
    self.data = [e] * (2 * self.size)
    self.lazy = [id] * (self.size)

  def update(self, k):
    self.data[k] = self.op(self.data[2 * k], self.data[2 * k + 1])

  def all_apply(self, k, f):
    self.data[k] = self.mapping(f, self.data[k])
    if k < self.size:
      self.lazy[k] = self.composition(f, self.lazy[k])

  def push(self, k): # 親の遅延配列の値を子に反映させる
    self.all_apply(2 * k, self.lazy[k])
    self.all_apply(2 * k + 1, self.lazy[k])
    self.lazy[k] = self.id

  def build(self, arr):
    #assert len(arr) == self.n
    for i, a in enumerate(arr):
      self.data[self.size + i] = a
    for i in range(self.size-1,0,-1):
      self.update(i)

  def set(self, p, x):
    #assert 0 <= p < self.n
    p += self.size
    #事前に関係のある遅延配列を全て反映させてしまう
    for i in range(self.log, 0, -1):
      self.push(p >> i)
    self.data[p] = x #値を更新する
    #関係のある区間の値も更新する
    for i in range(1, self.log + 1):
      self.update(p >> i)

  def get(self, p):
    #assert 0 <= p < self.n
    p += self.size
    #関係のある遅延配列を全て反映させる
    for i in range(1, self.log + 1):
      self.push(p >> i)
    return self.data[p]

  def prod(self, l, r):
    #assert 0 <= l <= r <= self.n
    if l == r: return self.e
    l += self.size
    r += self.size
    for i in range(self.log, 0, -1):
      if ((l >> i) << i) != l: self.push(l >> i)
      if ((r >> i) << i) != r: self.push(r >> i)
    sml = smr = self.e
    while l < r:
      if l & 1:
        sml = self.op(sml, self.data[l])
        l += 1
      if r & 1:
        r -= 1
        smr = self.op(self.data[r], smr)
      l >>= 1
      r >>= 1
    return self.op(sml, smr)

  def all_prod(self):
    return self.data[1]

  def apply(self, p, f):
    #assert 0 <= p < self.n
    p += self.size
    for i in range(self.log, 0, -1):
      self.push(p >> i)
    self.data[p] = self.mapping(f, self.data[p])
    for i in range(1, self.log + 1):
      self.update(p >> i)

  def range_apply(self, l, r, f):
    #assert 0 <= l <= r <= self.n
    if l == r: return
    l += self.size
    r += self.size
    for i in range(self.log, 0, -1):
      if ((l >> i) << i) != l: self.push(l >> i)
      if ((r >> i) << i) != r: self.push((r - 1) >> i)
    l2 = l
    r2 = r
    while l < r:
      if l & 1:
        self.all_apply(l, f)
        l += 1
      if r & 1:
        r -= 1
        self.all_apply(r, f)
      l >>= 1
      r >>= 1
    l = l2
    r = r2
    for i in range(1, self.log + 1):
      if ((l >> i) << i) != l: self.update(l >> i)
      if ((r >> i) << i) != r: self.update((r - 1) >> i)

  def max_right(self, l, g):
    #assert 0 <= l <= self.n
    #assert g(self.e)
    if l == self.n: return self.n
    l += self.size
    for i in range(self.log, 0, -1):
      self.push(l >> i)
    sm = self.e
    while True:
      while l % 2 == 0: l >>= 1
      if not g(self.op(sm, self.data[l])):
        while l < self.size:
          self.push(l)
          l = 2 * l
          if g(self.op(sm, self.data[l])):
            sm = self.op(sm, self.data[l])
            l += 1
        return l - self.size
      sm = self.op(sm, self.data[l])
      l += 1
      if (l & -l) == l: return self.n

  def min_left(self, r, g):
    #assert 0 <= r <= self.n
    #assert g(self.e)
    if r == 0: return 0
    r += self.size
    for i in range(self.log, 0, -1):
      self.push((r - 1) >> i)
    sm = self.e
    while True:
      r -= 1
      while r > 1 and r % 2: r >>= 1
      if not g(self.op(self.data[r], sm)):
        while r < self.size:
          self.push(r)
          r = 2 * r + 1
          if g(self.op(self.data[r], sm)):
            sm = self.op(self.data[r], sm)
            r -= 1
        return r + 1 - self.size
      sm = self.op(self.data[r], sm)
      if (r & -r) == r: return 0

###
def op(x, y):
    return (x[0]+y[0]+x[2]*y[1], x[1]+y[1], x[2]+y[2])

def mapping(p, x):
    if p == 1:
        return (x[1]*x[2]-x[0], x[2], x[1])
    else:
        return x

def composition(p, q):
    return p ^ q

###
def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    lst = LazySegmentTree(n, op, (0,0,0), mapping, composition, 0)

    # (inversion, num_0, num_1)
    for i in range(n):
        if a[i]:
            a[i] = (0, 0, 1)
        else:
            a[i] = (0, 1, 0)

    lst.build(a)

    ans = []
    for _ in range(q):
        t, l, r = list(map(int, input().split()))
        if t == 1:
            lst.range_apply(l-1, r, 1)
        else:
            ans.append(lst.prod(l-1, r)[0])

    print('\n'.join(map(str, ans)))

main()