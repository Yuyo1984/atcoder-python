mod = 998244353
a, b, c, d, e, f = map(lambda x: int(x) % mod, input().split())
x = (a * b) % mod
x = (x * c) % mod
y = (d * e) % mod
y = (y * f) % mod
print((x - y) % mod)
