s = input()
t = input()

char_set = set(["a", "t", "c", "o", "d", "e", "r"])

flag = False
for i in range(len(s)):
    if s[i] != t[i]:
        if s[i] == "@":
            if t[i] not in char_set:
                flag = True
        elif t[i] == "@":
            if s[i] not in char_set:
                flag = True
        else:
            flag = True
    if flag:
        print("You will lose")
        exit()
print("You can win")
