n, k = map(int, input().split())
box = [0] * k

i = 0
while n != 0:
    box[i] += 1
    n -= 1
    i += 1
    if i == k:
        i = 0

print(max(box) - min(box))
