N = int(input())
p = [*map(int, input().split())]
Q = [0] * n
m = 0
for i in range(1, n+1):
    m = P[i-1]
    Q[m-1] = i
print(" ".join(map(str, Q)))

