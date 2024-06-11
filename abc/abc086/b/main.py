a, b = input().split()
x = int(a + b)

for i in range(1, 334):
    if i**2 == x:
        print("Yes")
        exit()
print("No")
