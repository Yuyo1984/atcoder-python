import random
N = 100000
M = 0
for i in range(N):
    px = random.random()
    py = random.random()
    if (px ** 2 + py ** 2) <= 1.0:
        M += 1

print(4.0 * M / N)

