S = input()

x = len(S)
ans_set = set()

for i in range(x):
    for j in range(i, x):
        s = S[i:j+1]
        ans_set.add(s)

print(len(ans_set))

