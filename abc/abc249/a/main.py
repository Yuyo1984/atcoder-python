from sys import stdin
input = stdin.readline

a, b, c, d, e, f, x = map(int, input().split())

cnt_a = 0
cnt_b = 0
time1 = x
time2 = x

while time1 >= a:
    time1 -= a
    cnt_a += 1
    time1 -= c
    if time1 <= 0:
        time1 = 0

while time2 >= d:
    time2 -= d
    cnt_b += 1
    time2 -= f
    if time2 <= 0:
        time2 = 0

t_r = b * (a * cnt_a + time1)
a_r = e * (d * cnt_b + time2)

if t_r > a_r:
    print('Takahashi')
elif t_r < a_r:
    print('Aoki')
else:
    print('Draw')
