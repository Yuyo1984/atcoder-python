from sys import stdin
input = stdin.readline

S = input().rstrip()
T = input().rstrip()
ans = 1001
x = len(S)
y = len(T)
for i in range(x-y+1):
    U = S[i:i+y]
    change_strings = 0
    for j in range(y):
        if U[j] != T[j]:
            change_strings += 1
    if change_strings <= ans:
        ans = change_strings

print(ans)
