X = input()

N = len(X)
i = 0
while i < N:
    if X[i] == "c":
        if X[i + 1] != "h" or i == N - 1:
            print("NO")
            exit()
        else:
            i += 1
    elif X[i] not in ("o", "k", "u"):
        print("NO")
        exit()
    i += 1
print("YES")
