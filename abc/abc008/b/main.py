import collections

N = int(input())
d = collections.defaultdict(int)

for i in range(N):
    s = input()
    d[s] += 1


m_k = max(d, key=d.get)
print(m_k)
