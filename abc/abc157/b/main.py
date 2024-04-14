from sys import stdin
input = stdin.readline

A = []
for i in range(3):
    A.append([*map(int,input().split())])

N = int(input())
card = [[False for i in range(3)] for j in range(3)]

for i in range(N):
    b = int(input())
    for j in range(3):
        if b in A[j]:
            k = A[j].index(b)
            card[j][k] = True


if (card[0][0] and card[0][1] and card[0][2]) \
        or (card[1][0] and card[1][1] and card[1][2]) \
        or (card[2][0] and card[2][1] and card[2][2]) \
        or (card[0][0] and card[1][0] and card[2][0]) \
        or (card[0][1] and card[1][1] and card[2][1]) \
        or (card[0][2] and card[1][2] and card[2][2]) \
        or (card[0][0] and card[1][1] and card[2][2]) \
        or (card[0][2] and card[1][1] and card[2][0]):
            print("Yes")
else:
    print("No")

