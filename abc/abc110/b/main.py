n, m, x, y = map(int, input().split())
X = [*map(int, input().split())]
Y = [*map(int, input().split())]

for z in range(x + 1, y + 1):
    if all([i < z for i in X]) and all([i >= z for i in Y]):
        print("No War")
        exit()
print("War")
