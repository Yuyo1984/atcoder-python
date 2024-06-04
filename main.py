h, m = input().split(":")
h = int(h)
m = int(m)

h += 8
h %= 24
print(str(h) + ":" + str(m))
