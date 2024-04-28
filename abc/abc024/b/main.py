n, t = map(int, input().split())
a = int(input())
ans = 0
for i in range(n-1):
    b = int(input())
    if a+t <= b:
        ans += t
    else:
        ans += b - a
    a = b

ans += t
print(ans)

