# input
a, b = map(int, input().split())
l = [1, 2, 3]
# solve
if a == b:
    print(-1)
else:
    for x in l:
        if x != a and x != b:
            print(x)
            exit()
# output
