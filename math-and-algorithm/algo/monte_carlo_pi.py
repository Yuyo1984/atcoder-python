import random

N = 10000000
M = 0
for i in range(1, N+1):
    px = random.uniform(0, 1)
    py = random.uniform(0, 1)

    if (px ** 2 + py ** 2 <= 1.0):
        M += 1

print('{:.15f}'.format(4.0 * (M / N)))
