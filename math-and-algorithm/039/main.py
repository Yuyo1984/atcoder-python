N, Q = map(int, input().split())
s = [0] * (100009)
for i in range(Q):
    L, R, X = map(int, input().split())
    s[L] += X
    s[R + 1] -= X

ans = ""
for i in range(2, N + 1):
    if s[i] < 0:
        ans += ">"
    elif s[i] > 0:
        ans += "<"
    else:
        ans += "="

print(ans)
