N = int(input())
s = [input() for _ in range(N)]
M = int(input())
t = [input() for i in range(M)]

x = s + t
ans = 0
for i in x:
    h_m = s.count(i) - t.count(i)
    ans = max(h_m, ans)

print(ans)
