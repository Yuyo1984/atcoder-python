from sys import stdin
input = stdin.readline

N = int(input())
W = [*map(str, input().split())]
words = ["and", "not", "that", "the", "you"]
for i in words:
    if i in W:
        print("Yes")
        exit()

print("No")

