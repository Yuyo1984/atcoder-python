from sys import stdin
input = stdin.readline

n = int(input())
A = [*map(int, input().split())]

i = 0
while i < len(A) - 1:
     if abs(A[i]-A[i+1]) != 1:
        if A[i] < A[i+1]:
            A.insert(i+1, A[i]+1)
        elif A[i] > A[i+1]:
            A.insert(i+1, A[i]-1)
     i += 1

print(*A)
