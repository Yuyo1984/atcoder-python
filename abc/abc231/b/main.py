from sys import stdin
input = stdin.readline
from collections import Counter

N = int(input())
S = []
for i in range(N):
    S.append(input().rstrip())

S = Counter(S)
most_get = S.most_common(1)
print(most_get[0][0])
