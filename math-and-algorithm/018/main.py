N = int(input())
A = [*map(int, input().split())]

a = A.count(100)
b = A.count(200)
c = A.count(300)
d = A.count(400)

print((a*d)+(b*c))
