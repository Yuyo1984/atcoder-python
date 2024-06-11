x, y, z = map(int, input().split())

seats = x // (y + z)
if (x % (y + z)) < z:
    seats -= 1
print(seats)
