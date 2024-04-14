A, B, K = map(int, input().split())
x = min(A, K)
A -= x
K -= x
y = min(B, K)
B -= y
K -= y

print(A, B)

