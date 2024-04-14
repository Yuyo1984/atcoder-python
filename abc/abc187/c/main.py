from sys import stdin
input = stdin.readline

N = int(input())
S = set(input().rstrip() for i in range(N))

for s in S:
    if "!" + s in S:
        print(s)
        exit()

print("satisfiable")

