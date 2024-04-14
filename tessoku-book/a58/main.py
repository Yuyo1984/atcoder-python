class segmenttree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.data = [0] * (self.size * 2)

    def update(self, pos, x):
        pos += self.size
        self.data[pos] = x
        while pos >= 2:
            pos //= 2
            self.data[pos] = max(self.data[pos*2], self.data[pos*2 + 1])

    def query(self, l, r, a, b, u):
        if r <= a or b <= l:
            return -1000000000
        if l <= a and b <= r:
            return self.data[u]
        m = (a + b) // 2
        ansL = self.query(l, r, a, m, u * 2)
        ansR = self.query(l, r, m, b, u * 2 + 1)
        return max(ansL, ansR)

N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for i in range(Q)]

segT = segmenttree(N)
for q in queries:
    tp, *cont = q
    if tp == 1:
        pos, x = cont
        segT.update(pos-1, x)
    if tp == 2:
        l, r = cont
        ans = segT.query(l-1, r-1, 0, segT.size, 1)
        print(ans)

