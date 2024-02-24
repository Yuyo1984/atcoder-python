from sys import stdin
input = stdin.readline

n = int(input())
A = [*map(int, input().split())]
ans = 0
ansl = []
checker = [True] * n
for i in range(n):
    if checker[i] == True:
        checker[A[i]-1] = False

for i in range(n):
    if checker[i]:
        ans += 1
        ansl.append(i+1)

print(ans)
for i in range(len(ansl)):
    print(ansl[i], end=' ')
