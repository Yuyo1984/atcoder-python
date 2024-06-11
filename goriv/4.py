N = int(input())
A = set()
for i in range(N):
    A.add((tuple(input().split())))

print(len(A))
