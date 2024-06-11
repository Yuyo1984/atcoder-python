# input
n, a, b = map(int, input().split())
D = [*map(int, input().split())]
# solve
x = a + b
for i in range(n):
    D[i] %= x
D.sort()
D.append(D[0] + x)
flag = False
for i in range(1, n + 1):
    if D[i] - D[i - 1] > b:
        flag = True
# output
print("Yes" if flag else "No")
