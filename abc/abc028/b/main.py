S = input()
cnt = [0] * 6

for x in S:
    c = ord(x) - ord("A")
    cnt[c] += 1

print(*cnt)
