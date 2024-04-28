points = []
for i in range(5):
    points.append(int(input()))
k = int(input())

flag = False
l = len(points)
for i in range(l):
    for j in range(1, l):
        if points[j] - points[i] > k:
            flag = True
            break

if flag:
    print(":(")
else:
    print("Yay!")

