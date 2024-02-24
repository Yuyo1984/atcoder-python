from sys import stdin
input = stdin.readline

N = int(input())

for d in range(1, 13):
    for a in reversed(range(d-1)):
        for b in reversed(range(d-a-1)):
            c = d - a - b
            if N-1 == 0:
                pasprints
