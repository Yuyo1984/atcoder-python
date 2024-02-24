from sys import stdin
input = stdin.readline

S, W = map(int, input().split())

print('unsafe' if S<= W  else 'safe')
