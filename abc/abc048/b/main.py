def calc(y, x):
    if y == 0:
        return 0
    else:
        return y // x


a, b, x = map(int, input().split())
ans = calc(b, x) - calc(a - 1, x)

print(ans)
