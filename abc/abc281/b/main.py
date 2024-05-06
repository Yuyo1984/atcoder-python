def check(S):
    x = len(S)
    if x != 8:
        return False
    if not(S[0].isupper()):
        return False
    sand = S[1:-1]
    if not(sand.isdecimal()) or int(sand) < 100000 or int(sand) > 999999:
        return False
    if not(S[-1].isupper()):
        return False
    return True


S = input()
if check(S):
    print("Yes")
else:
    print("No")

