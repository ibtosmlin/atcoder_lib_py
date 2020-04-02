class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.ans = n*(n-1)//2      ######

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
    
        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x
        sx = self.size(x)          ######
        sy = self.size(y)          ######
        self.ans += sx*(sx-1)//2 + sy*(sy-1)//2   ######
        self.ans -= (sx+sy)*(sx+sy-1)//2          ######

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

######
N,M = map(int,input().split())
uf = UnionFind(N)
ans = [uf.ans]
pp = [list(map(int,input().split())) for i in range(M)]
for i in range(M,1,-1):
  uf.union(pp[i-1][0]-1, pp[i-1][1]-1)
  ans.append(uf.ans)
print('\n'.join(map(str, reversed(ans))))
