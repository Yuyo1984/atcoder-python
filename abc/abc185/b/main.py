N, M, T = map(int, input().split())
full = N
C = 0
flag = True
for i in range(M):
    A, B = map(int, input().split())
    full = full - (A - C)
    if full <= 0:
        flag = False
        break
    else:
        full = min(N, full + (B - A))
        C = B

full -= T - C
if full <= 0:
    flag = False
if flag:
    print("Yes")
else:
    print("No")
