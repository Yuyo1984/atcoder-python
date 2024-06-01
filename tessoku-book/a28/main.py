N = int(input())
ans = 0
for i in range(N):
    t, a = input().split()
    a = int(a)
    if t == "+":
        ans += a
    elif t == "-":
        ans -= a
    else:
        ans *= a
    ans %= 10000
    print(ans)
