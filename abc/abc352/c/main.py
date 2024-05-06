# func

# input
n = int(input())
hs_pair = []
for i in range(n):
    hs_pair.append(list(map(int, input().split())))
# solve
d = hs_pair[0][1] - hs_pair[0][0]
idx = 0
sum_head = hs_pair[0][0]
min_head = hs_pair[0][0]
max_shoulder = hs_pair[0][1]
for i in range(1, n):
    a = hs_pair[i][0]
    b = hs_pair[i][1]
    m = b - a
    sum_head += a
    if m >= d:
        d = m
        max_shoulder = b
        min_head = a

sum_head -= min_head

# answer
ans = sum_head + max_shoulder
print(ans)

