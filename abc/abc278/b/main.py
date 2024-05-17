def is_in_24hour(h, m):
    return 0 <= h <= 23 and 0 <= m <= 59


def misjudged(h, m):
    a = h // 10
    b = h % 10
    c = m // 10
    d = m % 10
    ac = 10 * a + c
    bd = 10 * b + d
    return is_in_24hour(ac, bd)


h, m = map(int, input().split())
while not misjudged(h, m):
    m += 1
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0

print(h, m)
