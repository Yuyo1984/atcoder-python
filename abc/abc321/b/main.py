from sys import stdin
input = stdin.readline

def score(x, A):
    min_A = x
    max_A = x
    sum_A = x
    for a in A:
        min_A = min(min_A, a)
        max_A = max(max_A, a)
        sum_A += a

    return sum_A - max_A - min_A

N, X = map(int, input().split())
A = [*map(int, input().split())]

ans = -1
for i in range(0, 101):
    if(score(i, A)) >= X:
        ans = i
        break

print(ans)
