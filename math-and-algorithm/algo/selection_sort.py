N = int(input())
A = [*map(int, input().split())]

for i in range(N):
    min_index = i
    min_value = A[i]
    for j in range(i+1, N):
        if A[j] < min_value:
            min_index = j
            min_value = A[j]
    A[i], A[min_index] = A[min_index], A[i]

print(*A)
