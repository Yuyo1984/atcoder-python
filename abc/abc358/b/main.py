# input
n, a = map(int, input().split())
T = [*map(int, input().split())]
# solve
n_t = 0
ansl = []
ansl.append(a + T[0])
for i in range(1, n):
    ansl.append(max(ansl[i - 1] + a, T[i] + a))

# output
for i in range(n):
    print(ansl[i])
