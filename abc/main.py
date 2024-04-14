def check(S, T):
    i = 0
    for t in T:
        while i < len(S) and S[i] != t:
            i += 1
        if i == len(S):
            return False
        i += 1
    return True


S = input().upper()
T = input()
if T[-1] != "x":
    if check(S, T):
        print("Yes")
    else:
        T = T[:-1]
        if check(S, T):
            print("Yes")
else:
    print("No")
