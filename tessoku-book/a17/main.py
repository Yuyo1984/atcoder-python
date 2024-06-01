N = int(input())
A = [0] * (100009)
tmp_line = [*map(int, input().split())]
for i, x in enumerate(tmp_line, start=2):
    A[i] = x
B = [0] * (100009)
tmp_line = [*map(int, input().split())]
for i, x in enumerate(tmp_line, start=3):
    B[i] = x


dp = [0] * (100009)

dp[1] = 0
dp[2] = A[2]
for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i])

ansl = []
place = N
while True:
    ansl.append(place)
    if place == 1:
        break

    if dp[place - 1] + A[place] == dp[place]:
        place -= 1
    else:
        place -= 2

print(len(ansl))
print(*ansl[::-1])
