n = int(input())
a = list(map(int, input().split()))
ans = 0

for i in range(n):
    x = a[i]
    for j in range(i, n):
        x = min(x, a[j])
        if all(val >= x for val in a[i:j+1]):
            cnt = x * (j-i+1)
            if cnt >= ans:
                ans = cnt

print(ans)
