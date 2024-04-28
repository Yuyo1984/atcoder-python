x = int(input())
A = [*map(int, input().split())]
m = max(A)
print(max([x for x in A if x != m]))

