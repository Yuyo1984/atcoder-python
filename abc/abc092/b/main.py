N = int(input())
D, X = map(int, input().split())
A = [int(input()) for i in range(N)]
ans = X
for a in A:
    ans += (D + a - 1) // a

print(ans)
