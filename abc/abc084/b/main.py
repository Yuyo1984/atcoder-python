a, b = map(int, input().split())
s = input()

if s[a] != "-":
    print("No")
    exit()
num_char = [str(i) for i in range(0, 10)]
for i in range(len(s)):
    if s[i] not in num_char and i != a:
        print("No")
        exit()
print("Yes")
