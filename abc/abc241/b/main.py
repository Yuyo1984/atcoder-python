n, m = map(int, input().split())
a = [*map(int, input().split())]
b = [*map(int, input().split())]

for pasta in b:
    if pasta in a:
        a.remove(pasta)
    else:
        print('No')
        exit()
print('Yes')

