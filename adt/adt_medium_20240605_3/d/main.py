# input
S = input()
# solve
for i in range(1, len(S)):
    if S[i - 1] == "B" and S[i] == "A":
        print("No")
        exit()
    if S[i - 1] == "C" and S[i] != "C":
        print("No")
        exit()
# output
print("Yes")
