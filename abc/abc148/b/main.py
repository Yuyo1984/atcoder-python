N = int(input())
strl = input().split(" ")

N *= 2
ans = ""
for i in range(N):
    if i % 2 == 0:
        ans += strl[0][i//2]
    else:
        ans += strl[1][i//2]

print(ans)

