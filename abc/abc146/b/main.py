import string
c = string.ascii_uppercase
N = int(input())
S = input()
ans = ""
for i in range(len(S)):
    x = (c.find(S[i]) + N) % 26
    ans += c[x]

print(ans)
