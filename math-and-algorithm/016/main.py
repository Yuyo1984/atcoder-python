def GCD(a, b):
    while a >= 1 and b >= 1:
        if a < b:
            b = b % a
        else:
            a = a % b
    if a >= 1:
        return a
    return b

n = int(input())
A = [*map(int, input().split())]
c = A[0]
for i in range(0, len(A)-1):
    c = GCD(c, A[i+1])

print(c)

