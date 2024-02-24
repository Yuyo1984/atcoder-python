from sys import stdin
input = stdin.readline

K = int(input())
for i in range(65, K+65):
    print(chr(i),end="")

