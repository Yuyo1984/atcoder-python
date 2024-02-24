import sys
input = sys.stdin.readline

K = int(input())
A, B = map(int, input().split())

for i in range(A, B+1):
    if i % K == 0:
        print('OK')
        sys.exit()

print('NG')
