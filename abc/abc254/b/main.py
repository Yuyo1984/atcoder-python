n = int(input())
l = []
for i in range(n+1):
    ll = []
    for j in range(i):
        if j == 0 or j == i-1:
            ll.append(1)
        else:
            ll.append(l[i-1][j-1] + l[i-1][j])
    l.append(ll)

for i in range(n+1):
    print(*l[i])

