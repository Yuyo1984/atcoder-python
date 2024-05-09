h, w = map(int, input().split())
a = []
for i in range(h):
    a.append(list(input()))

ans = []
for i in range(h+2):
    ans_l = []
    for j in range(w+2):
        if i == 0 or i == h+1 or j == 0 or j == w+1:
            ans_l.append('#')
        else:
            ans_l.append(a[i-1][j-1])
    ans.append(ans_l)

for i in range(h+2):
    print(''.join(ans[i]))

