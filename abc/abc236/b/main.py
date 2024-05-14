from collections import defaultdict

n = int(input())
a = [*map(int, input().split())]

number_dict = defaultdict(int)

for i in a:
    number_dict[i] += 1

x = [i for i, v in number_dict.items() if v == 3]
print(x[0])
