from sys import stdin
input = stdin.readline

S = input().rstrip()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
x = days.index(S) + 1
print(6 - x)

