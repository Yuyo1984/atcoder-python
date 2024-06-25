# input
x = [*map(int, input())]
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# solve
index = [number.index(x[i]) for i in range(4)]
if index[0] == index[1] == index[2] == index[3]:
    print("Weak")
    exit()
if (index[0] + 1) % 10 == index[1] % 10:
    if (index[1] + 1) % 10 == index[2] % 10:
        if (index[2] + 1) % 10 == index[3] % 10:
            print("Weak")
            exit()
# output
print("Strong")
