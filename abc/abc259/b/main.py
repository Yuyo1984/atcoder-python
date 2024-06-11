import math

a, b, d = map(int, input().split())
d = math.radians(d)
ans_x = a * math.cos(d) - b * math.sin(d)
ans_y = b * math.cos(d) + a * math.sin(d)
print(ans_x, ans_y)
