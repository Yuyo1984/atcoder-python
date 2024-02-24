from sys import stdin
input = stdin.readline

def rf(N):
    if N == 0:
        return 1
    else:
        return rf(N-1) * N
N = int(input())
print(rf(N))

