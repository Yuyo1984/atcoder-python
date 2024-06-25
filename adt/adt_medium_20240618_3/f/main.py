# input
N = int(input())
A = [*map(int, input().split())]
A.sort()
# solve
ans = 0
i = 0
while i < N - 1:
    if A[i] == A[i + 1]:
        ans += 1
        i += 1
    i += 1

# output
print(ans)
