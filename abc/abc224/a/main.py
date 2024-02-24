from sys import stdin
input = stdin.readline

s = input().rstrip()

if s[-2:] == 'er':
    print('er')
if s[-3:] == 'ist':
    print('ist')
