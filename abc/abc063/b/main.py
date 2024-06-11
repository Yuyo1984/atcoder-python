import string

S = input()

for i in string.ascii_lowercase:
    if S.count(i) >= 2:
        print("no")
        exit()
print("yes")
