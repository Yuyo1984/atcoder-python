from string import ascii_lowercase, ascii_uppercase

s = input()
upper = ascii_uppercase
lower = ascii_lowercase

counter = [0] * 150
flag1 = False
flag2 = False
flag3 = True
for i in range(len(s)):
    if s[i] in upper:
        flag1 = True
    if s[i] in lower:
        flag2 = True
    x = ord(s[i]) - ord("A")
    counter[x] += 1


for i in range(53):
    if counter[i] >= 2:
        flag3 = False

if flag1 and flag2 and flag3:
    print("Yes")
else:
    print("No")
