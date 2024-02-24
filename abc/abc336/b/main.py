from sys import stdin
input = stdin.readline

n = int(input())
x = bin(n)
ans = 0
for i in range(len(x)-1, 0, -1):
    if x[i] == "0":
        ans += 1
    else:
        print(ans)
        exit()
