n = int(input())
A = list(map(int, input().split()))
b = [0] * 4
p = 0
for i in range(n):
    b[0] += 1
    x = A[i]
    for j in range(3, -1, -1):
        if j + x >= 4:
            p += b[j]
            b[j] = 0
        else:
            b[j+x] += b[j]
            b[j] = 0

print(p)
