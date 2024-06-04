# input
N = int(input())
S = input()
mx = [0] * 26
# solve
l = 0
while l < N:
    r = l + 1
    while r < N and S[l] == S[r]:
        r += 1
    c = ord(S[l]) - ord("a")
    mx[c] = max(mx[c], r - l)
    l = r

# output
ans = sum(mx)
print(ans)
