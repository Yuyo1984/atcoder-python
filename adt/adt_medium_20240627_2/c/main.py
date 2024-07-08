# input
N, M = map(int, input().split())
A = [*map(int, input().split())]
B = [*map(int, input().split())]
# solve
for x in B:
    if x in A:
        A.remove(x)
    else:
        print("No")
        exit()

# output
print("Yes")
