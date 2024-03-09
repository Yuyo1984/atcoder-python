import sys
input = sys.stdin.readline

N, T = map(int, input().split())
points = [0] * N
for i in range(T):
    A, B = map(int, input().split())
    points[A-1] += B
    print(len(set(points)))

