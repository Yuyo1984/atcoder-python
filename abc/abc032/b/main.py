s = input()
k = int(input())

ans_set = set()

for i in range(0, len(s)):
    if i + k > len(s):
        break
    ans_set.add(s[i : i + k])

print(len(ans_set))
