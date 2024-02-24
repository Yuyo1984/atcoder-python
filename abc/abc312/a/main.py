from sys import stdin
input = stdin.readline

S = input().rstrip()
base = "ABCDEFG"
for i in range(len(base)):
    if base[i] + base[(i+2)%7] + base[(i+4)%7] == S:
        print("Yes")
        exit()

print("No")
