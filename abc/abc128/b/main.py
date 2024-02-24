N = int(input())
Book = []

for i in range(N):
    c, p = map(str, input().split())
    p = int(p)
    Book.append([(i+1), c, p])

Book = sorted(Book, key = lambda x : (x[1], -x[2]))

for i in range(N):
    print(Book[i][0])

