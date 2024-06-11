import collections

w = input()
cnt = collections.Counter()

for c in w:
    cnt[c] += 1

for x in cnt:
    if cnt[x] % 2 != 0:
        print("No")
        exit()
print("Yes")
