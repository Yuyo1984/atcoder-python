from sys import stdin
input = stdin.readline

N = int(input())
H = [*map(int, input().split())]

h = H[0]
x = 0
for i in range(1, N):
    if H[i] > h:
        h = H[i]
        x = i
    else:
        break

print(H[x])
