class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1 for i in range(n)]
        self.size = [1] * n

    def root(self, x):
        if self.parents[x] == -1:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def isSame(self, x, y):
        if self.root(x) == self.root(y):
            return True
        else:
            return False

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x

        self.parents[y] = x
        self.size[x] += self.size[y]

    def Size(self, x):
        return self.size[self.root(x)]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

def pos(i, j):
    return i * W + j

def neighber(i, j):
    lst = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == dj == 0:
                continue
            if 0 <= i + di < H and 0 <= j + dj < W:
                lst.append((i+di, j+dj))
    return lst

H, W = map(int, input().split())
field = [input() for i in range(H)]

uf = UnionFind(H * W + 1)
dot = H * W
for i in range(H):
    for j in range(W):
        if field[i][j] == '.':
            uf.unite(pos(i, j), dot)
            continue
        for i2, j2 in neighber(i, j):
            if field[i2][j2] == '#':
                uf.unite(pos(i, j), pos(i2, j2))

ans = uf.group_count() - 1
print(ans)

