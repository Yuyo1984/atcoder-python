from sys import stdin
input = stdin.readline

x = input()
flip = []
for i in x:
    if i == '0':
        flip.append('1')
    elif i == '1':
        flip.append('0')

print("".join(flip))
