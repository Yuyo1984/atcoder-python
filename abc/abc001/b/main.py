m = int(input())
m /= 1000
vv = ""

if m < 0.1:
    vv = "00"
elif 0.1 <= m <= 5.0:
    m *= 10
    m = int(m)
    vv = f'{m:02}'
elif 6.0 <= m <= 30:
    m += 50
    m = int(m)
    vv = str(m)
elif 35 <= m <= 70:
    m -= 30
    m //= 5
    m += 80
    m = int(m)
    vv = str(m)
else:
    vv = "89"

print(vv)

