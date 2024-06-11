# 解説AC
# 辞書とキューを使用してBFSを行う
import collections

# input
s = input()
d = collections.defaultdict(int)
q = collections.deque()

d[s] = 0
q.append(s)
# solve
while q:
    current = q.popleft()
    if current == "atcoder":
        print(d[current])
        exit()

    for i in range(1, 7):
        next = list(current)
        next[i - 1], next[i] = next[i], next[i - 1]
        next = "".join(next)
        if next not in d:
            q.append(next)
            d[next] = d[current] + 1

# output
