A = int(input())
B = int(input())

set1 = {A, B}
set2 = {1, 2, 3}

ans = set2 - set1

print(list(ans).pop())
