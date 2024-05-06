n, q = map(int, input().split())
s = input()
p = [0] * (n+1)
for i in range(1, n):
    if s[i-1] == s[i]:
        p[i] = p[i-1] + 1
    else:
        p[i] = p[i-1]
for i in range(q):
    l, r = map(int, input().split())
    ans = p[r-1] - p[l-1]
    print(ans)

