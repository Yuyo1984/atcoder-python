N = int(input())

X = str(N)

sum_x = 0
for i in X:
    sum_x += int(i)

if N % sum_x == 0:
    print("Yes")
else:
    print("No")
