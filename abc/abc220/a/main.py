from sys import stdin
input = stdin.readline

a, b, c = map(int, input().split())
flag = False

for i in range(a, b+1):
    if i % c == 0:
        print(i)
        flag = True
        break

if not flag:
    print(-1)
