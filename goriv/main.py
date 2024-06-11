def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


ans = 0
a, b = map(int, input().split())
for i in range(a, b):
    x = GCD(i, b)
    if x > ans:
        ans = x

print(ans)
