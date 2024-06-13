from string import ascii_lowercase

S = input()
low = ascii_lowercase

is_existed = [False] * 26

for c in S:
    if c in low:
        is_existed[low.index(c)] = True

for x in range(26):
    if not (is_existed[x]):
        print(low[x])
        exit()
print("None")
