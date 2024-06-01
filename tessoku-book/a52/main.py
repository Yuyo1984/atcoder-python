queue = []
Q = int(input())
for i in range(Q):
    query = list(input().split())
    if query[0] == "1":
        queue.append(query[1])
    elif query[0] == "2":
        print(queue[0])
    elif query[0] == "3":
        queue.remove(queue[0])
