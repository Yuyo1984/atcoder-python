from sys import stdin
input = stdin.readline

s = input()
cnt = 0
ans = 0
for i in range(len(s)):
    for j in range(len(s)):
        if s[j] == 'A' or s[j] == 'C' or \
            s[j] == 'G' or s[j] == 'T':
                cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0

print(ans)
