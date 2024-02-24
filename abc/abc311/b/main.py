from sys import stdin
input = stdin.readline

n, d = map(int, input().split())
S = []
for i in range(n):
    S.append(list(input()))

ansl = [True] * d

for i in range(d):
    for j in range(n):
        if S[j][i] == 'x':
            ansl[i] = False
            break

vac_list = []
temp = 0
for i in range(len(ansl)):
    if ansl[i] == True:
        temp += 1
    else:
        vac_list.append(temp)
        temp = 0
    if i == len(ansl) - 1:
        vac_list.append(temp)

print(max(vac_list))
