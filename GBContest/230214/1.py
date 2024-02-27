T = int(input())
ans = 0
for i in range(N):
    L, R = map(int, input().split())
    for a in range(L, R+1):
        for b in range(L, R+1):
            c = a + b
            if L <= c <= R:
                ans += 1
            if c > L or c > R:
                break

print(ans)

