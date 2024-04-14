N, M = map(int, input().split())
ans = 0
list_L = []
list_R = []
for i in range(1, M+1):
    L, R = map(int, input().split())
    list_L.append(L)
    list_R.append(R)

a = max(list_L)
b = min(list_R)

if a <= b:
    print(b-a+1)
else:
    print(0)
