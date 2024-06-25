w, a, b = map(int, input().split())
c = a + w
d = b + w

x = min(c, d) - max(a, b)

if c < b or d < a:
    print(abs(x))
else:
    print(0)
