from sys import stdin
input = stdin.readline

N = int(input())
A = [*map(int, input().split())]
log = []
for i in range(N):
    log.append(sum(A[7*i:7*i+7]))

print(*log)
