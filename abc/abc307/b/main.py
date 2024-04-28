def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False

N = int(input())
S = []
for i in range(N):
    S.append(input())

for i in range(N):
    for j in range(N):
        s = S[i] + S[j]
        if i != j and is_palindrome(s):
            print("Yes")
            exit()

print("No")
