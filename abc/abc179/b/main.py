from sys import stdin
input = stdin.readline

N = int(input())
counter = 0
for i in range(N):
    d1, d2 = map(int,input().split())
    if d1 == d2:
        counter += 1
        if counter == 3:
            print("Yes")
            exit()
    else:
        counter = 0

print("No")
