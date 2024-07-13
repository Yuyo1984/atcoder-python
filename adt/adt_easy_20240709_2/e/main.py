from collections import defaultdict

# 与えられた行列の転置行列を返す関数


def transposition(m):
    m = [list(x) for x in zip(*m)]
    return m


# input
h, w = map(int, input().split())
S = []
T = []
for i in range(h):
    S.append(list(input()))
S = transposition(S)
for i in range(h):
    T.append(list(input()))
T = transposition(T)
# solve
S = sorted(S)
T = sorted(T)
# output
for x in range(w):
    if S[x] != T[x]:
        print("No")
        exit()
print("Yes")
