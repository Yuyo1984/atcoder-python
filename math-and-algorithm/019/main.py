N = int(input())
A = [*map(int, input().split())]

x = A.count(1)
y = A.count(2)
z = A.count(3)

print(x * (x-1) // 2 + y * (y-1) // 2 + z * (z-1) // 2)
