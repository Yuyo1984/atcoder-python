import sys
input = sys.stdin.readline

N = int(input())
ansl = []
for i in range(1, N+1):
    if i % 3 == 0:
        ansl.append('x')
    else:
        ansl.append('o')

print(''.join(ansl))
