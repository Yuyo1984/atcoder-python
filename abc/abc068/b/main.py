from sys import stdin
input = stdin.readline

N = int(input())
ans = 0
while 2**(ans+1) <= N:
    ans += 1

print(2**ans)
