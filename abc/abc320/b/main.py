def is_palindrome(string):
    x = len(string)
    if string == string[::-1]:
        return x
    else:
        return -1

S = input()
ans = 0

x = len(S)
for i in range(x):
    for j in range(i, x):
        l = is_palindrome(S[i:j+1]) 
        if l >= ans:
            ans = l

print(ans)

