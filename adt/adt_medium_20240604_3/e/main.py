# input
N = int(input())
A = [*map(int, input().split())]
L = [A[0]]
# solve
for i in range(1, N):
    L.append(A[i])
    while True:
        if len(L) == 1:
            break
        if L[-1] != L[-2]:
            break
        L.pop()
        x = L.pop()
        L.append(x + 1)
# output
print(len(L))
