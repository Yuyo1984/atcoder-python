N = int(input())
P = [0] + [*map(int, input().split())]

x = P[N - 1]
idx = N - 1
ans = 0
while x != 0:
    idx = x - 1
    x = P[idx]
    ans += 1

print(ans)
