from itertools import product

N = int(input())
A = list(product(("a", "b", "c"), repeat=N))
for i in A:
    print("".join(i))
