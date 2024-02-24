import sys
input = sys.stdin.readline

N = input()

for i in range(3):
    if N[i] == '7':
        print('Yes')
        sys.exit()

print('No')
