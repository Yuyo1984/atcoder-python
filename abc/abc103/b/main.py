S = input()
T = input()
for i in range(len(S)):
    x = S[i:] + S[0:i]
    if x == T:
        print("Yes")
        exit()
print("No")
