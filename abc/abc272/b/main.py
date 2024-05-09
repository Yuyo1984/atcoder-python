n, m = map(int, input().split())
guest_list = []
checker = n * (n-1) // 2
for i in range(m):
    k, *x = map(int, input().split())
    guest_list.append(list(x))

cnt = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        for k in guest_list:
            if i in k and j in k:
                cnt += 1
                break

if checker == cnt:
    print("Yes")
else:
    print("No")
