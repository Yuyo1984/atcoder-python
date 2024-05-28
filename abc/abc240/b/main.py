N = int(input())
a = [*map(int, input().split())]
ans_set = set()

for x in a:
    ans_set.add(x)

print(len(ans_set))
