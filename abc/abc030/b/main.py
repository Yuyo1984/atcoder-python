n, m = map(int, input().split())

n %= 12
x = ((m * 60) + (n * 3600)) / 120
y = 6 * m

ans = abs(x - y)
if ans > 180:
    ans = 360 - ans
print(ans)
