# input
h, w, n = map(int, input().split())
# solve
A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)


S = sorted(list(set(A)))
T = sorted(list(set(B)))
ranking_a = {x: i + 1 for i, x in enumerate(S)}
ranking_b = {x: i + 1 for i, x in enumerate(T)}

# output
for i in range(n):
    print(ranking_a[A[i]], ranking_b[B[i]])
