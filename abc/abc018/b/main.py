S = input()
N = int(input())

ans = S
for i in range(N):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    ans = ans[0:l] + ans[l : r + 1][::-1] + ans[r + 1 :]

print(ans)
