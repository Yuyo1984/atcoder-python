from sys import stdin
input = stdin.readline

s = input().rstrip()

for i in range(10):
    if str(i) not in s:
        print(i)
        break
