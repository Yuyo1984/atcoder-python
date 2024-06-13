N = int(input())
A = [int(input()) for i in range(N)]
A = sorted(list(set(A)))
print(A[-2])
