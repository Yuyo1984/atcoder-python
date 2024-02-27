N, X = map(int, input().split())
A = [*map(int, input().split())]

A.sort()
left = 0
right = N - 1
while left <= right:
    mid = (left + right) // 2
    if A[mid] == X:
        print("Yes")
        exit()
    elif A[mid] > X:
        right = mid - 1
    else:
        left = mid + 1

print("No")

