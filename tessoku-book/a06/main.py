n, q = map(int, input().split())
a = [0] + [*map(int, input().split())]
s = [0] * (n+1)
for i in range(1 , n+1):
    s[i] = s[i-1] + a[i]

for i in range(q):
    l, r = map(int, input().split())
    print(s[r] - s[l-1])
