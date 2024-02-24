from sys import stdin
input = stdin.readline

n = int(input().rstrip())
s = input().rstrip()

if s[n-1] == 'o':
    print('Yes')
else:
    print('No')
