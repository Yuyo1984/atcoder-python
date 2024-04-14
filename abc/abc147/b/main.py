S = input()
x = len(S) // 2
A = S[0:x]
B = S[x:len(S)]
B = B[::-1]

ans = 0
for i in range(x):
    if A[i] != B[i]:
        ans += 1

print(ans)

