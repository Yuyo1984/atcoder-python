# input
n, k = map(int, input().split())
A = [*map(int, input().split())]
# solve
ans = 0
seats = k
i = 0
while True:
    if i == n:
        break
    if seats < A[i]:
        ans += 1
        seats = k
    seats -= A[i]
    i += 1
ans += 1
# output
print(ans)
