# input
N = int(input())
A = [*map(int, input().split())]
# solve
ans = 0
for i in range(1, N + 1):
    d = A[i - 1]
    for j in range(1, d + 1):
        flag = True
        x = str(i) + str(j)
        for k in range(len(x) - 1):
            if x[k] != x[k - 1]:
                flag = False
                break
        if flag:
            ans += 1

# output
print(ans)
