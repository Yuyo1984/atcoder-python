from sys import stdin
input = stdin.readline

from atcoder.string import suffix_array

N = int(input())
P = list(map(int, input().rstrip().split()))
P = suffix_array(P)
P = [x + 1 for x in P]

print(*P)
