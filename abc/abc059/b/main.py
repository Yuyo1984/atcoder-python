from sys import stdin
input = stdin.readline

A = input()
B = input()

if len(A) < len(B):
    print("LESS")
elif len(A) > len(B):
    print("GREATER")
else:
    if A > B:
        print("GREATER")
    elif A < B:
        print("LESS")
    else:
        print("EQUAL")

