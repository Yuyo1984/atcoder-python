from sys import stdin
input = stdin.readline

def S(str):
    a = list(map(int, list(str)))
    return sum(a)

A, B = map(str, input().split())

print(max(S(A), S(B)))

