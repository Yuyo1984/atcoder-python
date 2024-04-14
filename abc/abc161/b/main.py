from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
A = [*map(int, input().split())]

choice = 0
sum_vote = sum(A)
for i in range(N):
    if A[i] * 4 * M >= sum_vote:
        choice += 1

if choice >= M:
    print("Yes")
else:
    print("No")

