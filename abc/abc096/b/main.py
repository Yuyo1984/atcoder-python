a, b, c = map(int, input().split())
k = int(input())

ans = 0
m = max(a, b, c)
if m == a:
    ans = 2**k * a + b + c
elif m == b:
    ans = 2**k * b + c + a
else:
    ans = 2**k * c + a + b

print(ans)
