x, a, b = map(int, input().split())
s = abs(a - x)
t = abs(b - x)
if s < t:
    print('A')
else:
    print('B')
