from sys import stdin
input = stdin.readline

S = []
for i in range(4):
    S.append(input().rstrip())

for i in range(3):
    for j in range(i+1, 4):
        if S[i] == S[j]:
            print("No")
            exit()

print("Yes")
