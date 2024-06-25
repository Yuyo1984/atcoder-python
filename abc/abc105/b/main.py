N = int(input())
a = N // 4
b = N // 7

for i in range(a + 1):
    for j in range(b + 1):
        if 4 * i + 7 * j == N:
            print("Yes")
            exit()
print("No")
