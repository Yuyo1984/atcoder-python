S = input()

W_l = ['Sunny', 'Cloudy', 'Rainy']

index = W_l.index(S) + 1
if index == 3:
    index = 0

print(W_l[index])
