def is_palindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True


a, b = map(int, input().split())
ans = 0
for i in range(a, b + 1):
    if is_palindrome(i):
        ans += 1

print(ans)
