a, b, c = map(int, input().split())

x = max(a, b, c)

if x == a:
    print(b * c // 2)
elif x == b:
    print(a * c // 2)
else:
    print(a * b // 2)
