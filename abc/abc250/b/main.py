n, a, b = map(int, input().split())
g = []
for i in range(5):
    for row in range(a):
        g.append(("." * b + "#" * b) * 5)
    for row in range(a):
        g.append(("#" * b + "." * b) * 5)

for row in range(a*n):
    print(g[row][:b * n])
