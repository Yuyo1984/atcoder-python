N = int(input())
seats = [False for _ in range(100001)]

for i in range(N):
    l, r = map(int, input().split())
    seats[l : r + 1] = [True] * (r + 1 - l)

print(seats.count(True))
