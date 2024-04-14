import math
N = int(input())
A = [*map(int, input().split())]

x = math.prod(A)
y = 0
for i in range(len(A)):
    y += math.prod(A) // A[i]

print(x / y)

