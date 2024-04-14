from sys import stdin
input = stdin.readline

N = int(input())
L = [*map(int, input().split())]
ans = 0
L.sort()
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if L[i] != L[j] and L[j] != L[k] and L[i] != L[k] and (L[i] + L[j] > L[k]):
                ans += 1

print(ans)
