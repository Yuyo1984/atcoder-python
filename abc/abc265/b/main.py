N, M, T = map(int, input().split())
A = [*map(int, input().split())]
xy = {}
for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    xy[x] = y

for i in range(N - 1):
    T -= A[i]
    if i in xy:
        T += xy[i]
    if T <= 0:
        print("No")
        exit()

print("Yes")
