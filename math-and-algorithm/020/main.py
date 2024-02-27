N = int(input())
A = [*map(int, input().split())]

ans = 0
x = len(A)
for i in range(x):
    for j in range(i+1, x):
        for k in range(j+1, x):
            for l in range(k+1, x):
                for m in range(l+1, x):
                    if A[i] + A[j] + A[k] + A[l] + A[m] == 1000:
                        ans += 1

print(ans)

