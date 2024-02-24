r, d, x_ts = map(int, input().split())

for i in range(10):
    x_ts = r * x_ts - d
    print(x_ts)
