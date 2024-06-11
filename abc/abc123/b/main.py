def wait_to_order(x):
    while x % 10 != 0:
        x += 1
    return x


import itertools

time = [int(input()) for i in range(5)]
time_permutations = list(itertools.permutations(time))
ans = 643
for t in time_permutations:
    n_t = 0
    for i in range(5):
        if i != 4:
            n_t += wait_to_order(t[i])
        else:
            n_t += t[i]
    if n_t < ans:
        ans = n_t


print(ans)
