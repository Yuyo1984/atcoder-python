# input
N = int(input())
poems = []
op = set()
points = []
for i in range(N):
    s, t = input().split()
    t = int(t)
    if s not in op:
        op.add(s)
        poems.append([s, i + 1])
        points.append(t)

# solve
x = max(points)
print(poems[points.index(x)][1])
# output
