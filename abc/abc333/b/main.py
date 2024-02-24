from sys import stdin
input = stdin.readline

s = input().rstrip()
t = input().rstrip()

len = 'ABCDEAEDCBA'

if (s in len and t in len) or (s not in len and t not in len):
    print('Yes')
else:
    print('No')
