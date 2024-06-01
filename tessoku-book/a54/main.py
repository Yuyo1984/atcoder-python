Q = int(input())
d = {}
for i in range(Q):
    query = list(input().split())
    if query[0] == "1":
        name = query[1]
        point = int(query[2])
        d[name] = point
    elif query[0] == "2":
        name = query[1]
        print(d[name])
