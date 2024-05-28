N, M = map(int, input().split())
A = [*map(int, input().split())]
B = [*map(int, input().split())]
C = A + B
C.sort()
flag = False
for i in range(1, len(C)):
    if C[i - 1] in A and C[i] in A:
        flag = True
if flag:
    print("Yes")
else:
    print("No")
