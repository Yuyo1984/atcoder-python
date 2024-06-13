n, a, b = map(int, input().split())
n_p = 0

for i in range(n):
    s, d = input().split()
    d = int(d)
    if s == "East":
        if d < a:
            n_p += a
        elif d > b:
            n_p += b
        else:
            n_p += d
    else:
        if d < a:
            n_p -= a
        elif d > b:
            n_p -= b
        else:
            n_p -= d

if n_p < 0:
    print("West", -n_p)
elif n_p > 0:
    print("East", n_p)
else:
    print(n_p)
