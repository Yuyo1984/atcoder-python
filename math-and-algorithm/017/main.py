def GCD(A, B):
    while A >= 1 and B >= 1:
        if A < B:
            B %= A
        else:
            A %= B
    if A >= 1:
        return A
    return B

def LCM(A, B):
    return A * B // GCD(A, B)

N = int(input())
A = [*map(int, input().split())]
quo_list = []
a = A[0]
for i in range(1, len(A)):
    a = GCD(a, A[i])

A = list(map(lambda x:x//a, A))

b = A[0]
for i in range(1, len(A)):
    b = LCM(b, A[i])

print(a * b)

