n, k = map(int, input().split())

if k % 2 == 0 and k >= 2 * n - 2:
    print("Yes")
else:
    print("No")
