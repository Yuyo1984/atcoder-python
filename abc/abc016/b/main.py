a, b, c = map(int, input().split())
x = a + b
y = a - b
if x == c and y == c:
    print("?")
elif x == c:
    print("+")
elif y == c:
    print("-")
else:
    print("!")
