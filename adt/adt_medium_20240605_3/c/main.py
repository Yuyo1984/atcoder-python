# input
N = int(input())
S = [*map(int, input().split())]
area_set = set()
ans = 0
# solve
for i in range(1, 334):
    for j in range(1, 334):
        area = 4 * i * j + 3 * i + 3 * j
        if 1 <= area <= 1000:
            area_set.add(area)

for x in S:
    if x not in area_set:
        ans += 1

# output
print(ans)
