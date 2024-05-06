n, m = map(int, input().split())
a = [*map(int, input().split())]
p_p = []
o_m = []
prob = []
for i in range(n):
    s = input()
    b = a[:]
    b.remove(a[i])
    m = max(b)
    o_m.append(m)
    point = i+1
    for j in range(m):
        not_ans = []
        if s[i] == 'o':
            point += a[i]
        else:
            not_ans.append(i)
    p_p.append(point)
    prob.append(not_ans)

for i in range(n):
    prob_points = []
    n_a = prob[i]
    for j in range(len(n_a)):
        prob_points.append(a[n_a[j]])

