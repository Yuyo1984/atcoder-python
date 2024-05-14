a = int(input())
b = int(input())
n = int(input())

x = n
while x % a != 0 or x % b != 0:
    x += 1

print(x)
