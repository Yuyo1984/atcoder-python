N, T = map(int, input().split())
ans = 1010
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        if c <= ans:
            ans = c
if ans == 1010:
    print("TLE")
else:
    print(ans)
