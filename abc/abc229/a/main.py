from sys import stdin
input = stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

if (s1[0] == '.' and s2[1] == '.') or (s1[1] == '.' and s2[0] == '.'):
    print('No')
else:
    print('Yes')
