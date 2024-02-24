from sys import stdin
input = stdin.readline
import re

s = input().rstrip()

B_indexes = []
K_index = 0
R_indexes = []
for i in range(8):
    if s[i] == 'B':
        B_indexes.append(i+1)
    if s[i] == 'K':
        K_index = i+1
    if s[i] == 'R':
        R_indexes.append(i+1)

if (B_indexes[0] % 2) != (B_indexes[1] % 2) and \
    R_indexes[0] < K_index < R_indexes[1]:
        print('Yes')
else:
    print('No')
