from sys import stdin
input = stdin.readline

S = [*map(int, input().split())]
for i in range(len(S)-1):
    if S[i] % 25 != 0:
        print("No")
        exit()
    if not(100 <= S[i] <= 675):
        print("No")
        exit()
    if S[i] > S[i+1]:
        print("No")
        exit()

print("Yes")

