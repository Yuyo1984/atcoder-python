from sys import stdin
input = stdin.readline

N = int(input())
ST = []
for i in range(N):
    ST.append(list(map(str, input().split())))

ST = sorted(ST, reverse=True, key=lambda x: int(x[1]))

print(ST[1][0])
