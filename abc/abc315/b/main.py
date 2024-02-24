from sys import stdin
input = stdin.readline

m = int(input())
D = [*map(int, input().split())]

days_of_years = sum(D)

middle_day = (days_of_years+1) // 2

sum = 0
counter = 0
while sum < middle_day:
    sum += D[counter]
    if sum >= middle_day:
        break
    counter += 1

progress = 0
for i in range(counter):
    progress += D[i]
rest_days = middle_day - progress

print(counter+1, rest_days)