N = int(input())
ans = 10**10
for i in range(N):
    a, p, x = map(int, input().split())
    x -= a
    if x > 0 and p < ans:
        ans = p

if ans == 10**10:
    ans = -1
print(ans)
