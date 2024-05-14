a, d = map(int, input().split())

x = (a + 1) * d
y = a * (d + 1)
if x > y:
    print(x)
else:
    print(y)
