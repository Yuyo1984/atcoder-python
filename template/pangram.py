N = int(input())
w = list(input().split())
s = ''
for word in w:
    s += word

counter = [0] * 26

for i in s:
    counter[ord(i)-ord('a')] += 1

print(*counter)
if all([i >= 1 for i in counter]):
    print("Yes")
else:
    print("No")
