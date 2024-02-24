from sys import stdin
input = stdin.readline

n = int(input())
ans = list('-' * (n+2))
for i in range(0, n+1):
    for j in range(1, 10):
        if n % j == 0:
            if i % (n/j) == 0:
                ans[i+1] = str(j)
                break

print(''.join(ans[1:n+2]))