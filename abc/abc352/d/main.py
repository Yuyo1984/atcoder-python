# func

# input
n, k = map(int, input().split())
p = [*map(int,input().split())]
p_d = {}
for i in range(n):
    p_d[p[i]] = i+1
# solve
ans = float('inf')
p_d = sorted(p_d.items())
for i in range(n - k):
    group = [p_d[i][1] for i in range(i, i+k)]
    r = max(group)
    l = min(group)
    for j in p_d:
        if j[1] == r:
            r = j[0]
        if j[0] == l:
            l = j[0]
    diff = r - l
    print()
    if diff <= ans:
        ans = diff

# answer
print(ans)
    
