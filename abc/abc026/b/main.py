N = int(input())
R = [int(input()) for _ in range(N)]
R.sort()

pi = 3.14159265358979

x = 0
flag = 1
for i in range(N - 1, -1, -1):
    if flag:
        x += R[i] ** 2
    else:
        x -= R[i] ** 2
    flag ^= 1

print(x * pi)
