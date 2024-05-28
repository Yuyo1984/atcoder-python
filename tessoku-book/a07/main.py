d = int(input())
n = int(input())
d_r = [0] * (d+2)
s_d = [0] * (d+2)

for i in range(n):
    l, r = map(int, input().split())
    d_r[l] += 1
    d_r[r+1] -= 1

for i in range(1, d+1):
    s_d[i] = s_d[i-1] + d_r[i]

for i in range(1, d+1):
    print(s_d[i])
