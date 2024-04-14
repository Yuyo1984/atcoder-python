N = int(input())
A = [*map(int, input().split())]

flag = True
for i in range(N):
    if A[i] % 2 == 0:
        if A[i] % 3 != 0 and A[i] % 5 != 0:
            flag = False
            break

if flag:
    print("APPROVED")
else:
    print("DENIED")

