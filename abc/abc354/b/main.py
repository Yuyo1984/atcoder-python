import collections
#input
n = int(input())
n_r = collections.defaultdict(int)
sum_rating = 0
#solve
for i in range(n):
    name, rating = input().split()
    n_r[name] = int(rating)
    sum_rating += int(rating)

n_r = sorted(n_r.items(), key=lambda x:x[0])
winner = sum_rating % n

#output
print(n_r[winner][0])
