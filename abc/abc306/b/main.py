def calc(A):
    ans = 0
    for i in range(64):
        if A[i] == 1:
            ans += 2 ** i
    return ans

A = [*map(int, input().split())]
print(calc(A))

