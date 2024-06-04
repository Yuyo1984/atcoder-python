from math import sqrt

ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

BAx = ax - bx
BAy = ay - by
BCx = cx - bx
BCy = cy - by
CAx = ax - cx
CAy = ay - cy
CBx = bx - cx
CBy = by - cy

pattern = 2
if (BAx * BCx + BAy * BCy) < 0:
    pattern = 1
if (CAx * CBx + CAy * CBy) < 0:
    pattern = 3

ans = 0.0
if pattern == 1:
    ans = sqrt(BAx * BAx + BAy * BAy)
if pattern == 3:
    ans = sqrt(CAx * CAx + CAy * CAy)
if pattern == 2:
    S = abs(BAx * CAy - BAy * CAx)
    BCL = sqrt(BCx * BCx + BCy * BCy)
    ans = S / BCL

print(f"{ans:0.7f}")
