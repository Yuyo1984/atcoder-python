N = int(input())
prime = [True for _ in range(10**8)]

# sieve of eratosthenes
i = 2
while i * i <= N:
    if prime[i]:
        for x in range(2 * i, N + 1, i):
            prime[x] = False
    i += 1

for i in range(2, N + 1):
    if prime[i]:
        print(i)
